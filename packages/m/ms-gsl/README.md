# ms-gsl

URL: [GSL](https://github.com/microsoft/GSL)

----

The Guidelines Support Library (GSL) contains functions and types that are suggested for use by the C++ Core Guidelines maintained by the Standard C++ Foundation. This repo contains Microsoft's implementation of GSL.

The entire implementation is provided inline in the headers under the gsl directory. The implementation generally assumes a platform that implements C++14 support.

While some types have been broken out into their own headers (e.g. gsl/span), it is simplest to just include gsl/gsl and gain access to the entire library.
