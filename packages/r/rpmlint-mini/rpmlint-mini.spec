#
# spec file for package rpmlint-mini
#
# Copyright (c) 2022 SUSE LLC
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


Name:           rpmlint-mini
Version:        %(rpm -q rpmlint --qf '%%{VERSION}')
Release:        0
Summary:        RPM file correctness checker
License:        GPL-2.0-or-later
URL:            http://rpmlint.zarb.org/
Source0:        desktop-file-utils-0.24.tar.xz
Source1:        stdlib.txt
Source2:        rpmlint.wrapper
Source3:        rpmlint-mini.rpmlintrc
# need to fetch the file from there
BuildRequires:  checkbashisms
BuildRequires:  dash
BuildRequires:  glib2-devel
BuildRequires:  glib2-devel-static
BuildRequires:  libedit-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  rpmlint >= 2
#!BuildIgnore:  rpmlint-mini
Requires:       cpio
Requires:       polkit-default-privs

%description
rpmlint is a tool to check common errors on RPM packages. Binary and
source packages can be checked.

%prep
%setup -q -n desktop-file-utils-0.24
[ -r COPYING ]

%build
%configure
pushd src
make %{?_smp_mflags} desktop-file-validate V=1 DESKTOP_FILE_UTILS_LIBS="%{_libdir}/libglib-2.0.a -lpthread -lrt"
popd

%install
# Check that rpmlint works at all
set +e
%{_bindir}/rpmlint -i rpmlint
test $? -gt 0 -a $? -lt 60 && exit 1
set -e
# Build a virtual env
python3 -m venv %{buildroot}/opt/testing
# We don't need pip, or activation
%{buildroot}/opt/testing/bin/pip uninstall -y pip
rm %{buildroot}/opt/testing/bin/activate*
# We need these available
cp -a src/desktop-file-validate %{buildroot}/opt/testing/bin
cp -a %{_bindir}/dash %{_bindir}/checkbashisms %{buildroot}/opt/testing/bin
cp -a %{_libdir}/libedit.so.0* %{buildroot}/opt/testing/lib
# Install config files
install -d -m 755 %{buildroot}/opt/testing/share
cp -a %{_sysconfdir}/xdg/rpmlint %{buildroot}/opt/testing/share
# Override configs are selectively taken from rpmlint-strict
rm -f %{buildroot}/opt/testing/share/rpmlint/*.override.toml
# Python standard library, rpmlint dependencies, and the interpreter
pushd %{_libdir}/python%{py3_ver}
for file in $(cat %{SOURCE1}); do
  exp=$(ls -1 $file)
  install -D -m 644 $exp %{buildroot}/opt/testing/lib/python%{py3_ver}/$exp
done
popd
cp -a %{python_sitearch}/{rpm,zstd,zstandard}* %{buildroot}/opt/testing/lib/python%{py3_ver}/site-packages
cp -a %{python_sitelib} %{buildroot}/opt/testing/lib/python%{py3_ver}
cp -a %{_libdir}/libpython%{py3_ver}*.so.* %{buildroot}/opt/testing/lib
cp -a %{_libdir}/libexpat*.so.* %{buildroot}/opt/testing/lib
cp -a %{_libdir}/libmpdec*.so.* %{buildroot}/opt/testing/lib || echo "Skipping libmpdec.so"
cp -a %{_bindir}/python3 %{buildroot}/opt/testing/bin
cp -a %{_bindir}/python%{py3_ver} %{buildroot}/opt/testing/bin
pushd %{buildroot}/opt/testing/lib/python%{py3_ver}/
for f in $(find -name \*.py | sort) ; do
  PYTHONOPTIMIZE=1 python3 -O -m compileall -b $f
  rm $f
done
popd
find %{buildroot}/opt/testing/ -name __pycache__  -exec rm -rf {} +
# We need to force the shebang to be under /opt/testing
sed -e 's,/usr,/opt/testing,' %{_bindir}/rpmlint > %{buildroot}/opt/testing/bin/rpmlint.real
chmod a+x %{buildroot}/opt/testing/bin/rpmlint.real
rm -rf %{buildroot}/{usr,etc}
install -m 755 -D %{SOURCE2} %{buildroot}/opt/testing/bin/rpmlint
# We don't want requirements of libraries, or the odd shebang
%define __requires_exclude (^lib.*|python3)$
# We don't want to provide any libraries, or Python modules we ship
%define __provides_exclude ^(lib|python)

%files
/opt/testing
%license COPYING

%changelog
