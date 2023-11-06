
We use `make` for our automated builds.

The structure of a `makefile`:

```
target: dependencies
	instructions on how to build target
```

We can include make instructions from another file, and we can call `make` from `make`.

We will use `common.mk` in the top-level directory to hold common make targets.

Other makefiles will `include` that file.

