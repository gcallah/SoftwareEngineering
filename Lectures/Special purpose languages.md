First, every CS student should understand the idea of a [Universal Turing Machine](https://en.wikipedia.org/wiki/Universal_Turing_machine) and the [Church-Turing Thesis](https://en.wikipedia.org/wiki/Church–Turing_thesis). The practical import of these ideas is that all general-purpose computers, and all general-purpose programming languages, can compute anything any other general-purpose computer or language can compute. (Some of them might be much slower than others, or make it easier to express a computation.)

You are familiar with lots of general-purpose languages: C, C++, C#, Java, Python, JavaScript, Pascal, Fortran, Cobol, Perl, Rust, Go, Lisp, Clojure, Haskell... there are *many*! (Rule 110)

But there are also many *special purpose languages*: these languages may or may not be [Turing complete](https://en.wikipedia.org/wiki/Turing_completeness), but at the very least they do not advertise themselves as such: they exist to help in solving problems in some special domain of computing.

Why should we use a language that is restricted in this way? Well, it might make it *much easier* to solve problems in its own domain: the very fact that a hammer is designed primarily for driving in nails makes it much better at that job than a [Swiss army knife](https://en.wikipedia.org/wiki/Swiss_Army_knife), or a stone.

We will employ several special purpose languages in our course:

| Language | Primary Use |
| -------- | ------- |
| Shell | Run other programs |
| Make | Build a digital artifact |
| YAML | Specify some configuration |
| Markdown | Format text |
| HTTP | Transfer hypertext over the Internet |
| HTML | Describe the structure of a Web page |

Another very common special purpose language, which we will *not* be using, is SQL, designed for querying and updating databases.

A final, very important point here, is that you can make your own special purpose language: it need not be fancy or complex! Let's look at an example. (Form filler.)

## Examples

UNIX shell example ([Knuth vs. McIlroy](https://franklinchen.com/blog/2011/12/08/revisiting-knuth-and-mcilroys-word-count-programs/#:~:text=Knuth%20came%20up%20with%20a,level%20and%20complicated%20when%20unnecessary.))


## Note

YAML is an example of a declarative language: it states what should be the case, but (generally) not how it is achieved.

Styles of computer language:

* functional (Lisp)
* procedural (C)
* object-oriented (Java)
* declarative (YAML)













