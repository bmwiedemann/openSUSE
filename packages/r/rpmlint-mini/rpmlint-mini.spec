#
# spec file for package rpmlint-mini
#
# Copyright (c) 2025 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


# This works regardless of the primary python3 flavor. The stdlib.txt and
# install section depend on the python 3.11 layout.
%define python_flavor %{primary_python}
%define my_python %{expand:%{__%{python_flavor}}}

Name:           rpmlint-mini
Version:        %(rpm -q rpmlint --qf '%%{VERSION}')
Release:        0
Summary:        RPM file correctness checker
License:        GPL-2.0-or-later
URL:            https://github.com/rpm-software-management/rpmlint
Source0:        desktop-file-utils-0.26.tar.xz
Source1:        stdlib.txt
Source2:        rpmlint.wrapper
Source3:        rpmlint-mini.rpmlintrc

# PATCH-FEATURE-OPENSUSE desktop-file-utils-suse-keys.patch vuntz@opensuse.org -- Handle SUSE-specific keys in validator. This is not strictly necessary, since they are prefixed with X-, but we can verify that the value has the right type.
Patch0:         desktop-file-utils-suse-keys.patch
# PATCH-FIX-UPSTREAM -- SingleMainWindow is present in xdg-specs 1.5 and can be used by both GNOME and KDE
Patch2:         0001-validate-support-SingleMainWindow-key-from-1.5.patch
Patch3:         0002-validate-Support-version-1.5.patch

# need to fetch the file from there
BuildRequires:  checkbashisms
# the main package rpmlint's python3 runtime requirements do not necessarily match our target flavor
BuildRequires:  %{python_flavor}-base
BuildRequires:  %{python_flavor}-importlib-metadata
BuildRequires:  %{python_flavor}-packaging
BuildRequires:  %{python_flavor}-pybeam
BuildRequires:  %{python_flavor}-pyenchant
BuildRequires:  %{python_flavor}-python-magic
BuildRequires:  %{python_flavor}-pyxdg
BuildRequires:  %{python_flavor}-rpm
BuildRequires:  %{python_flavor}-tomli
BuildRequires:  %{python_flavor}-tomli-w
BuildRequires:  %{python_flavor}-xml
BuildRequires:  %{python_flavor}-zstandard
BuildRequires:  dash
BuildRequires:  glib2-devel
BuildRequires:  glib2-devel-static
BuildRequires:  libedit-devel
BuildRequires:  libtool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  rpmlint >= 2
#!BuildIgnore:  rpmlint-mini
Requires:       cpio
Requires:       polkit-default-privs

%description
rpmlint is a tool to check common errors on RPM packages. Binary and
source packages can be checked.

%prep
%autosetup -p1 -n desktop-file-utils-0.26

%build
%meson
%meson_build

%install
# Check that rpmlint works at all, with the primary flavor
set +e
%{_bindir}/rpmlint -i rpmlint
test $? -gt 0 -a $? -lt 60 && exit 1
set -e
# Check that we have all required python modules in the target flavor
for p in $(rpm -q --requires rpmlint | grep '^python3-'); do
  rpm -q --whatprovides ${p/python3-/%{python_flavor}-}
done
# Build a virtual env
%my_python -m venv %{buildroot}/opt/testing --without-pip --copies
# We don't need activation
rm %{buildroot}/opt/testing/bin/activate*
# We need these available
cp -a %{_vpath_builddir}/src/desktop-file-validate %{buildroot}/opt/testing/bin
cp -a %{_bindir}/dash %{_bindir}/checkbashisms %{buildroot}/opt/testing/bin
cp -a %{_bindir}/{tar,gzip} %{buildroot}/opt/testing/bin
cp -a %{_libdir}/libedit.so.0* %{buildroot}/opt/testing/lib
# Install config files
install -d -m 755 %{buildroot}/opt/testing/share
cp -a %{_sysconfdir}/xdg/rpmlint %{buildroot}/opt/testing/share
# Override configs are selectively taken from rpmlint-strict
rm -f %{buildroot}/opt/testing/share/rpmlint/*.override.toml
# Python standard library, rpmlint dependencies, and the interpreter
pushd %{_libdir}/python%{python_version}
for file in $(cat %{SOURCE1}); do
  if [ -f $file ]
  then
      exp=$(ls -1 $file)
      install -D -m 644 $exp %{buildroot}/opt/testing/lib/python%{python_version}/$exp
  fi
done
popd
ldd %{python_sitearch}/rpm/*.so | while read L T R A
do
# skip libc/libm, they must match the system ld.so (which we cannot replace)
case $L in lib[cm].*) continue;; esac
cp '-aLt%{buildroot}/opt/testing/lib' "${R}" || # is it a virtual library?
! <"${R}" || # it is a real library and still could not be copied
false # this is necessary to really fail
done
cp -a %{python_sitearch}/{rpm,zstandard}* \
%{buildroot}/opt/testing/lib/python%{python_version}/site-packages
cp -a %{python_sitelib} %{buildroot}/opt/testing/lib/python%{python_version}
cp -a %{python3_sitelib}/rpmlint* %{buildroot}/opt/testing/lib/python%{python_version}
cp -a %{_libdir}/libpython%{python_version}*.so.* %{buildroot}/opt/testing/lib
cp -a %{_libdir}/libexpat*.so.* %{buildroot}/opt/testing/lib
cp -a %{_libdir}/libmpdec*.so.* %{buildroot}/opt/testing/lib || echo "Skipping libmpdec.so"
pushd %{buildroot}/opt/testing/lib/python%{python_version}/
rm -r site-packages/meson*
for f in $(find -name \*.py | sort) ; do
  PYTHONOPTIMIZE=1 %{my_python} -O -m compileall -b $f
  rm $f
done
popd
find %{buildroot}/opt/testing/ -name __pycache__  -exec rm -rf {} +
# Change the script-interpreter line to use our custom python venv in /opt/testing
sed -e '1s,#!.*python.*,#!/opt/testing/bin/python3,' %{_bindir}/rpmlint > %{buildroot}/opt/testing/bin/rpmlint.real

chmod a+x %{buildroot}/opt/testing/bin/rpmlint.real
rm -rf %{buildroot}/{usr,etc}
install -m 755 -D %{SOURCE2} %{buildroot}/opt/testing/bin/rpmlint
# We don't want requirements of libraries, or the odd shebang
%define __requires_exclude (^lib.*|python3)$
# We don't want to provide any libraries, or Python modules we ship
%define __provides_exclude ^(lib|python)

%check
# check rpmlint-mini with the custom flavor
%meson_test
sed -e 's|/opt|%{buildroot}/opt|' -e 's|exec|%my_python|' %{buildroot}/opt/testing/bin/rpmlint > myrpmlint
chmod +x myrpmlint
set +e
sh -x myrpmlint -i rpmlint
test $? -gt 0 -a $? -lt 60 && exit 1
set -e

%files
/opt/testing
%license COPYING

%changelog
