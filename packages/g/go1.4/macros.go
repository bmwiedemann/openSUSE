# Macros for Go module building.
#
# Copyright: (c) 2011 Sascha Peilicke <saschpe@gmx.de>
# Copyright: (c) 2012 Graham Anderson <graham@andtech.eu>
# Copyright: (c) 2015 SUSE Linux GmbH
#


%go_ver         %(LC_ALL=C rpm -q --qf '%%{epoch}:%%{version}\\n' go | sed -e 's/(none)://' -e 's/ 0:/ /' | grep -v "is not")
%go_arch        GOARCH
%go_build_ver   %(go version | sed 's/^go version //' | sed 's:\/::g' | tr -d ' ' | cut -c 1-7 )

%go_dir          %{_libdir}/go1.4
%go_sitedir      %{_libdir}/go1.4/pkg
%go_sitearch     %{_libdir}/go1.4/pkg/linux_%{go_arch}
%go_contribdir     %{_libdir}/go1.4/contrib/pkg/linux_%{go_arch}
%go_contribsrcdir  %{_datadir}/go1.4/contrib/src/
%go_tooldir        %{_datadir}/go1.4/pkg/tool/linux_%{go_arch}

%go_exclusivearch \
ExclusiveArch:  %ix86 x86_64 %arm

%go_provides \
%go_exclusivearch \
Provides:       %{name}-devel = %{version} \
Provides:       %{name}-devel-static = %{version}

# Prepare the expected Go package build environement.
# We need a $GOPATH: go help gopath
# We need a valid importpath: go help packages
%goprep() \
export GOPATH=%{_builddir}/go \
if [ %# -eq 0 ]; then \
  echo "goprep: please specify a valid importpath, see: go help packages" \
  exit 1 \
else \
  export IMPORTPATH=%1 \
fi \
# create the importpath and move the package there \
pkg_dir=$(basename $PWD) \
cd %{_builddir} \
mkdir -p $GOPATH/src/$IMPORTPATH \
(shopt -s dotglob; mv -- ${pkg_dir}/* $GOPATH/src/$IMPORTPATH) \
# now link the old location to the new (for compatibility)\
rmdir ${pkg_dir} \
ln -s $GOPATH/src/$IMPORTPATH ${pkg_dir} \
cd ${pkg_dir} \
# we'll be installing packages/binaries/tools, make the targ dirs \
install -d %{buildroot}%{go_contribdir} \
install -d %{buildroot}%{go_tooldir} \
install -d %{buildroot}%{_bindir} \
%{nil}

# %%gobuild macro actually performs the command "go install", but the go
# toolchain will install to the $GOPATH which allows us then customise the final
# install for the distro default locations.
#
# gobuild accepts zero or more arguments. Each argument corresponds to
# a modifier of the importpath. If no arguments are passed, this is equivalent
# to the following go install statement:
#
#     go install [importpath]
#
# Only the first or last arguement may be ONLY the wildcard argument "..."
# if the wildcard argument is passed then the importpath expands to all packages
# and binaries underneath it. If the argument contains only the wildcard no further
# arguments are considered.
#
# If no wildcard argument is passed, go install will be invoked on each $arg
# subdirectory under the importpath.
#
# Valid importpath modifier examples:
#
#    example:  %gobuild ...
#    command:  go install importpath...
#
#    example:  %gobuild /...
#    command:  go install importpath/...      (All subdirs NOT including importpath)
#
#    example:  %gobuild foo...
#    command:  go install importpath/foo...   (All subdirs INCLUDING foo)
#
#    example:  %gobuild foo ...               (same as foo...)
#    command:  go install importpath/foo...   (All subdirs INCLUDING foo)
#
#    example:  %gobuild foo/...
#    commands: go install importpath/foo/...  (All subdirs NOT including foo)
#
#    example:  %gobuild foo bar
#    commands: go install importpath/foo
#              go install importpath/bar
#
#    example:  %gobuild foo ... bar
#    commands: go install importpath/foo...   (bar is ignored)
#
#    example:  %gobuild foo bar... baz
#    commands: go install importpath/foo
#              go install importpath/bar...
#              go install importpath/baz
#
# See: go help install, go help packages
%gobuild() \
export BUILDFLAGS="-s -v -p 4 -x" \
export GOPATH=%{_builddir}/go:%{_libdir}/go1.4/contrib \
export GOBIN=%{_builddir}/go/bin \
MOD="" \
if [ %# -gt 0 ]; then \
  for mod in %*; do \
    if [ $mod == "..." ]; then \
      MOD=$MOD... \
      if [ "$WITH_FAKE_BUILDID" = "true" ] ; then \
	go install $BUILDFLAGS -ldflags "-B 0x$(head -c20 /dev/urandom | od -An -tx1 | tr -d ' \\n')" $IMPORTPATH$MOD \
      else \
	go install $BUILDFLAGS $IMPORTPATH$MOD \
      fi \
      break \
    else \
      MOD=/$mod \
      if [ "$WITH_FAKE_BUILDID" = "true" ] ; then \
        go install $BUILDFLAGS -ldflags "-B 0x$(head -c20 /dev/urandom | od -An -tx1 | tr -d ' \\n')" $IMPORTPATH$MOD \
      else \
        go install $BUILDFLAGS $IMPORTPATH$MOD \
      fi \
    fi \
  done \
else \
  if [ "$WITH_FAKE_BUILDID" = "true" ] ; then \
    go install $BUILDFLAGS -ldflags "-B 0x$(head -c20 /dev/urandom | od -An -tx1 | tr -d ' \\n')" $IMPORTPATH \
  else \
    go install $BUILDFLAGS $IMPORTPATH \
  fi \
fi \
%{nil}

# Install all compiled packages and binaries to the buildroot
%goinstall() \
export GOPATH=%{_builddir}/go \
install -d %{buildroot}%{go_contribdir} \
TMPPKG=%{_builddir}/go/pkg \
if [ "$(ls -A $TMPPKG)" ]; then \
	cp -ar %{_builddir}/go/pkg/linux_%{go_arch}/* %{buildroot}%{go_contribdir} \
fi \
TMPBIN=%{_builddir}/go/bin \
if [ "$(ls -A $TMPBIN)" ]; then \
     install -m755 $TMPBIN/* %{buildroot}%{_bindir} \
fi \
%{nil}

%gofix() \
export GOPATH=%{_builddir}/go \
if [ %# -eq 0 ]; then \
  echo "gofix: please specify a valid importpath, see: go help fix" \
  exit 1 \
else \
  go fix %1... \
fi \
%{nil}

%gotest() \
export GOPATH=%{_builddir}/go:%{_libdir}/go1.4/contrib  \
if [ %# -eq 0 ]; then \
  echo "gotest: please specify a valid importpath, see: go help test" \
  exit 1 \
else \
  go test -x %1... \
fi \
%{nil}

%gosrc() \
install -d %{buildroot}%{go_contribsrcdir} \
cd %{_builddir}/go/src \
find . -name "*.go" -exec install -Dm644 \{\} %{buildroot}%{go_contribsrcdir}/\{\} \\; \
%{nil}

# Template for source sub-package
%gosrc_package(n:r:) \
%package %{-n:-n %{-n*}-}source \
Summary: Source codes for package %{name} \
Group: Development/Sources \
Requires: %{-n:%{-n*}}%{!-n:%{name}} = %{version} \
%{-r:Requires: %{-r*}} \
Provides: %{-n:%{-n*}}%{!-n:%{name}}-doc = %{version}-%{release} \
Obsoletes: %{-n:%{-n*}}%{!-n:%{name}}-doc < %{version}-%{release} \
%description %{-n:-n %{-n*}-}source \
This package provides source codes for package %{name}.\
%{nil}

# backward compatibility
%go_requires    \
%(if [ ! -f /usr/lib/rpm/golang.attr ] ; then \
echo "Requires: go1.4 >= %go_build_ver" \
fi) \
%{nil}

%go_recommends %{nil}

%godoc \
%gosrc \
%{nil}

# Template for doc sub-package
%godoc_package(n:r:) \
%package %{-n:-n %{-n*}-}doc \
Summary: API documention for package %{name} \
Group: Documentation/Other \
Requires: %{-n:%{-n*}}%{!-n:%{name}} = %{version} \
%{-r:Requires: %{-r*}} \
%description %{-n:-n %{-n*}-}doc \
This package provides API, examples and documentation \
for package %{name}.\
%{nil}
