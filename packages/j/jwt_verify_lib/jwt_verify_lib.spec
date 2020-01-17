#
# spec file for package jwt_verify_lib
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define src_install_dir /usr/src/%{name}

Name:           jwt_verify_lib
Version:        20191024
Release:        0
Summary:        JSON Web Tokens verification library for C++
License:        Apache-2.0
Group:          Development/Libraries/C and C++
Url:            https://github.com/google/%{name}
Source0:        %{name}-%{version}.tar.xz
Patch0:         jwt_verify-make-compatible-with-openssl.patch
BuildRequires:  fdupes
BuildArch:      noarch

%description
jwt_verify_lib is a library which verifies JSON Web Tokens. It does not provide
any other features like signing or advanced checks.

%package source
Summary:        Source code of jwt_verify_lib
Group:          Development/Sources

%description source
jwt_verify_lib is a library which verifies JSON Web Tokens. It does not provide
any other features like signing or advanced checks.

This package contains source code of jwt_verify_lib.

%prep
%autosetup -p1

%build

%install
mkdir -p %{buildroot}%{src_install_dir}
cp -r * %{buildroot}%{src_install_dir}
%fdupes %{buildroot}%{src_install_dir}

%files source
%license LICENSE
%doc README.md
%{src_install_dir}

%changelog
