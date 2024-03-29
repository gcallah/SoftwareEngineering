# A template makefile that works for static websites.
# Need to export TEMPLATE_DIR as ENV var
export TEMPLATE_DIR = templates
# Export MARKDOWN_DIR
export MARKDOWN_DIR = md
PTML_DIR = html_src
UTILS_DIR = utils
DOCKER_DIR = docker
# REPO = this repo!

INCS = $(TEMPLATE_DIR)/head.txt $(TEMPLATE_DIR)/logo.txt $(TEMPLATE_DIR)/menu.txt

HTMLFILES = $(shell ls $(PTML_DIR)/*.ptml | sed -e 's/.ptml/.html/' | sed -e 's/html_src\///')

PTMLFILES = $(shell ls $(MARKDOWN_DIR)/*.md | sed -e 's/.md/.ptml/' | sed -e 's/$(MARKDOWN_DIR)/$(PTML_DIR)/')

FORCE:

tests: FORCE
	echo "Here is where you should run your tests."

%.html: $(PTML_DIR)/%.ptml $(INCS)
	python3 $(UTILS_DIR)/html_checker.py $<
	$(UTILS_DIR)/html_include.awk <$< >$@
	git add $@

local: $(HTMLFILES)

$(PTML_DIR)/%.ptml: $(MARKDOWN_DIR)/%.md
	# Requires pandoc, uses commonmark flavor of markdown
	pandoc -f commonmark -t html5 <$< >$@

ptml: $(PTMLFILES)

github:
	-git commit -a 
	git push origin master

prod: $(INCS) $(HTMLFILES) tests github

submods:
	git submodule foreach 'git pull origin master'
	
nocrud:
	rm *~
	rm .*swp
	rm $(PTML_DIR)/*~
	rm $(PTML_DIR)/.*swp

clean:
	touch $(PTML_DIR)/*.ptml; make local
