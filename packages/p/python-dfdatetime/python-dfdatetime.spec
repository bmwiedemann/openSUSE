#
# spec file for package python-dfdatetime
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


%define timestamp 20220925
%define modname dfdatetime
Name:           python-dfdatetime
Version:        0~%{timestamp}
Release:        0
Summary:        Digital Forensics date and time (dfDateTime)
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/log2timeline/dfdatetime
Source:         https://github.com/log2timeline/%{modname}//releases/download/%{timestamp}/%{modname}-%{timestamp}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
dfDateTime, or Digital Forensics date and time, provides date and time
objects to preserve accuracy and precision.

%prep
%setup -q -n %{modname}-%{timestamp}

%build
%python_build

%install
%python_install
# setup.py install helpfully installs files where it shouldn’t
rm -rfv %{buildroot}%{_datadir}/doc/%{modname}

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v tests/*.py

%files %{python_files}
%license LICENSE
%doc ACKNOWLEDGEMENTS AUTHORS README
%{python_sitelib}/dfdatetime
%{python_sitelib}/dfdatetime-%{timestamp}*info

%changelog
