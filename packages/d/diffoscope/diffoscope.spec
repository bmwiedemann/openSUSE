#
# spec file for package diffoscope
#
# Copyright (c) 2024 SUSE LLC
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


Name:           diffoscope
Version:        272
Release:        0
Summary:        In-depth comparison of files, archives, and directories
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://diffoscope.org/
Source0:        https://diffoscope.org/archive/diffoscope-%{version}.tar.bz2
Source1:        https://diffoscope.org/archive/diffoscope-%{version}.tar.bz2.asc
Source2:        diffoscope.keyring
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-base >= 3.7
BuildRequires:  python3-curses
BuildRequires:  python3-libarchive-c
BuildRequires:  python3-pytest
BuildRequires:  python3-python-magic
BuildRequires:  python3-setuptools
Requires:       python3-curses
Requires:       python3-libarchive-c
Requires:       python3-python-magic
Requires:       python3-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
# Tools required for proper function of this program
# in extras_require
Recommends:     python3-distro
Recommends:     python3-argcomplete
Recommends:     python3-defusedxml
Recommends:     python3-jsondiff
Recommends:     python3-progressbar
# for getfacl
Suggests:       acl
# for ar, readelf, objcopy and objdump
Suggests:       binutils
Suggests:       bzip2
# for img2txt
Suggests:       caca-utils
# for isoinfo
Suggests:       cdrkit-cdrtools-compat
# for cbfstool
Suggests:       coreboot-utils
# for stat
Suggests:       coreutils
Suggests:       cpio
# for cmp and diff
Suggests:       diffutils
# for lsattr
Suggests:       e2fsprogs
# for ppudump
Suggests:       fpc
# for msgunfmt
Suggests:       gettext-tools
# for ghc
Suggests:       ghc-compiler
Suggests:       gzip
# for pedump
Suggests:       mono-devel
Suggests:       pdftk
# for pdftotext
Suggests:       poppler-tools
# for RPM unpacking
Suggests:       python3-rpm
Suggests:       sqlite3
# for unsquashfs
Suggests:       squashfs
# for zipinfo
Suggests:       unzip
# for xxd
Suggests:       vim
Suggests:       xz
# currently missing:
# enjarify, javap, lipo, otool, showttf, sng
BuildArch:      noarch

%description
diffoscope will try to get to the bottom of what makes files or
directories different. It will recursively unpack archives of many kinds
and transform various binary formats into more human readable form to
compare them. It can compare two tarballs, ISO images, or PDF just as
easily.

It can be scripted through error codes, and a report can be produced
with the detected differences. The report can be text or HTML.
When no type of report has been selected, diffoscope defaults
to write a text report on the standard output.

diffoscope is developed as part of the `“reproducible builds” Debian
project <https://wiki.debian.org/ReproducibleBuilds>`_.
It is meant to be able to quickly understand why two builds of the same
package produce different outputs. diffoscope was previously named
debbindiff.

%prep
%autosetup -p1
sed -i '0,/#!\/usr\/bin\/env/ d' diffoscope/main.py

%build
%python3_build

%install
%python3_install
%fdupes %{buildroot}%{python3_sitelib}/
mv %{buildroot}%{_bindir}/diffoscope %{buildroot}%{_bindir}/diffoscope-%{py3_ver}
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
ln -s -f %{_sysconfdir}/alternatives/diffoscope %{buildroot}%{_bindir}/diffoscope
touch %{buildroot}%{_sysconfdir}/alternatives/diffoscope

%post
%{_sbindir}/update-alternatives --install \
    %{_bindir}/diffoscope diffoscope %{_bindir}/diffoscope-%{py3_ver} 10

%postun
if [ "$1" = 0 ] ; then
    %{_sbindir}/update-alternatives --remove diffoscope %{_bindir}/diffoscope-%{py3_ver}
fi

%check
# test_identification https://salsa.debian.org/reproducible-builds/diffoscope/-/issues/98
# comparators/test_python/test_diff https://salsa.debian.org/reproducible-builds/diffoscope/-/issues/284#note_280561
py.test-%{python3_bin_suffix} -k 'not ((test_python and test_diff) or test_identification)'

%files
%doc README.rst
%license COPYING
%{_bindir}/diffoscope
%{_bindir}/diffoscope-%{py3_ver}
%{python3_sitelib}/diffoscope
%{python3_sitelib}/diffoscope-%{version}*-info
%ghost %{_sysconfdir}/alternatives/diffoscope

%changelog
