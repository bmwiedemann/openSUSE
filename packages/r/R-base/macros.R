# R-related variables
%R_archlib   %{_libdir}/R/library
%R_noarchlib %{_datadir}/R/library
%R_version   @vers@

# Get a version number that is compatible with RPM
# Provide the package version as the argument.
# Only needed if there are dashes or underscores
# in the version number.
%R_rpmver() %( echo %1 | tr - . | tr _ . )

# Setup th build directory the right way.
# By default %{packname} is used.
# Override this with "-p [name]".
%R_unpack(p:) %setup -q -c -n %{-p:%{-p*}}%{!-p:%{packname}}

# Install the package
# By default %{packname} is used.
# Override this with "-p [name]".
# By default, the package is stored in the architecture-dependent
# R library directory.  Use the "-n" flag to install in the
# architecture-independent directory.
# Manually specify a directory using "-t [path]".
%R_install(np:t:) \
    %define curpack %{-p:%{-p*}}%{!-p:%{packname}} \
    %define curlib %{-t:%{-n:%{error:Can't specify both -t and -n}}%{!-n:%{-t*}}}%{!-t:%{-n:%{R_noarchlib}}%{!-n:%{R_archlib}}} \
    mkdir -p %{buildroot}%{curlib} \
    %{_bindir}/R CMD INSTALL -l %{buildroot}%{curlib} %{curpack}  \
    test -d %{curpack}/src && (cd %{curpack}/src; rm -f *.o *.so) \
    rm -f %{buildroot}%{curlib}/R.css \
%{nil}

# Run standard R tests.
# By default %{packname} is used.
# Override this with "-p [name]".
%R_test(p:) %{_bindir}/R CMD check %{-p:%{-p*}}%{!-p:%{packname}}
