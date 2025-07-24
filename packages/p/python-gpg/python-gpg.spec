#
# spec file for package python-gpg
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           python-gpg
Version:        2.0.0
Release:        0
Summary:        Python bindings for GnuPG
License:        LGPL-2.1-or-later
# https://dev.gnupg.org/source/gpgmepy.git
URL:            https://gnupg.org/software/gpgme/index.html
Source:         https://www.gnupg.org/ftp/gcrypt/gpgmepy/gpgmepy-%{version}.tar.bz2
Source1:        https://www.gnupg.org/ftp/gcrypt/gpgmepy/gpgmepy-%{version}.tar.bz2.sig
# 0xDF4475BB0CEDF389 retrieved via WKD
# see https://lists.gnupg.org/pipermail/gnupg-devel/2025-June/035955.html
Source2:        %{name}.keyring
Patch0:         python-gpg-COPY_FILES.patch
Patch1:         python-gpg-nobetasuffix.patch
# PATCH-FIX-UPSTREAM build-pep621-pyproject.patch bsc#[0-9]+ mcepl@suse.com
# clean up pyproject.toml for switch to wheel-based build
Patch2:         build-pep621-pyproject.patch
%ifarch %{ix86} %{arm}
Patch3:         gpgmepy-2.0.0-swig-32-bit.patch
%endif
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 65.2.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  swig
BuildRequires:  pkgconfig(gpg-error) >= 1.47
BuildRequires:  pkgconfig(gpgme) >= 1.7.0
%python_subpackages

%description
This package contains Python bindings for GnuPG

%prep
%autosetup -p1 -n gpgmepy-%{version}

%build
%ifarch %{ix86} %{arm}
# explicitly pass the large file options, because we build gpgme with it
export CFLAGS="%{optflags} -D_FILE_OFFSET_BITS=64"
%endif
autoreconf -fiv
%configure \
    --with-libgpg-error-prefix=%{_libdir} \
    --with-gpgme-prefix=%{_libdir} \
    %{nil}

ln -sf "./src" gpg
touch copystamp
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}/%{_prefix}

%files %{python_files}
%license COPYING COPYING.LESSER
%{python_sitearch}/gpg
%{python_sitearch}/gpg-%{version}.dist-info

%changelog
