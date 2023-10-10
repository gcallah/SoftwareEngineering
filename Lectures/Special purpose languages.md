First, every CS student should understand the idea of a [Universal Turing Machine](https://en.wikipedia.org/wiki/Universal_Turing_machine) and the [Church-Turing Thesis](https://en.wikipedia.org/wiki/Church–Turing_thesis). The practical import of these ideas is that all general-purpose computers, and all general-purpose programming languages, can compute anything any other general-purpose computer or language can compute. (Some of them might be much slower than others, or make it easier to express a computation.)

You are familiar with lots of general-purpose languages: C, C++, C#, Java, Python, JavaScript, Pascal, Fortran, Cobol, Perl, Rust, Go, Lisp, Clojure, Haskell... there are *many*!

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

A final, very important point here, is that you can make your own special purpose language: it need not be fancy or complex! Let's look at an example.









