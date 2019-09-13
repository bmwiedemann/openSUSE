#
# spec file for package python-dfdatetime
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define timestamp 20190517
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-dfdatetime
Version:        0~%{timestamp}
Release:        0
Summary:        Digital Forensics Date and Time (dfDateTime)
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/log2timeline/dfdatetime
Source:         https://github.com/log2timeline/dfdatetime/releases/download/%{timestamp}/dfdatetime-%{timestamp}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
#Python-mock is used for internal self-test at a minimum
Requires:       python-mock
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%python_subpackages

%description
dfDateTime, or Digital Forensics date and time, provides date and time objects to preserve accuracy and precision.

%prep
%setup -q -n dfdatetime-%{timestamp}

%build
%python_build

%install
%python_install
# these doc files are installed to the wrong place
rm -rf %{buildroot}/usr/share/doc/dfdatetime
%fdupes %{buildroot}/%{_prefix}

%files %{python_files}
%defattr(-,root,root)
%license LICENSE
%doc ACKNOWLEDGEMENTS AUTHORS README
%{python_sitelib}/dfdatetime*

%changelog
