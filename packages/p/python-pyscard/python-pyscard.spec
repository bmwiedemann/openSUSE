#
# spec file for package python-pyscard
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2011 LISA GmbH, Bingen, Germany.
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


%define modname pyscard
Name:           python-pyscard
Version:        2.0.10
Release:        0
Summary:        Python module adding smart card support
License:        LGPL-2.0-or-later
Group:          Development/Languages/Python
URL:            https://pyscard.sourceforge.io/
Source:         https://files.pythonhosted.org/packages/source/p/pyscard/pyscard-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  pcsc-lite-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  swig
Requires:       pcsc-ccid
%python_subpackages

%description
Python-pyscard consists of smartcard.scard, an extension module wrapping
Windows smart card base components (also known as PCSC) on Windows and PCSC
lite on linux and Mac OS X Tiger and Leopard, and smartcard, a higher level
python framework built on top of the raw PCSC API.

%prep
%setup -q -n %{modname}-%{version}
mv smartcard/doc .
dos2unix LICENSE

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
mv smartcard smartcard_hide
%pyunittest_arch discover -v

%files %{python_files}
%doc ChangeLog doc README.md
%license LICENSE
%{python_sitearch}/pyscard*
%{python_sitearch}/smartcard

%changelog
