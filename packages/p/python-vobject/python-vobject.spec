#
# spec file for package python-vobject
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


%global modname vobject
%{?sle15_python_module_pythons}
Name:           python-vobject
Version:        0.9.8
Release:        0
Summary:        Python package for parsing and creating iCalendar and vCard files
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/py-vobject/vobject/
Source:         https://files.pythonhosted.org/packages/source/v/vobject/%{modname}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/py-vobject/vobject/pull/87 remove six
Patch0:         no-six.patch
BuildRequires:  %{python_module PyICU}
BuildRequires:  %{python_module devel >= 2.7}
BuildRequires:  %{python_module python-dateutil >= 2.7.0}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-python-dateutil >= 2.7.0
Requires:       python-pytz
Requires(post): update-alternatives
Requires(preun): update-alternatives
Recommends:     python-PyICU
Provides:       %{modname} = %{version}
Obsoletes:      %{modname} < 0.9.2
BuildArch:      noarch
%python_subpackages

%description
Parses iCalendar and vCard files into Python data structures,
decoding the relevant encodings. Also serializes vobject data
structures to iCalendar, vCard, or (experimentally) hCalendar
unicode strings.

%prep
%autosetup -p1 -n %{modname}-%{version}
# Fix wrong-file-end-of-line-encoding
sed -i 's/\r$//' ACKNOWLEDGEMENTS.txt

%build
%python_build

%install
%python_install
for p in change_tz ics_diff ; do
    %python_clone -a %{buildroot}%{_bindir}/$p
done
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v tests.py

%post
%python_install_alternative change_tz
%python_install_alternative ics_diff

%postun
%python_uninstall_alternative change_tz
%python_uninstall_alternative ics_diff

%files %{python_files}
%license LICENSE-2.0.txt
%doc ACKNOWLEDGEMENTS.txt README.md
%python_alternative %{_bindir}/change_tz
%python_alternative %{_bindir}/ics_diff
%{python_sitelib}/%{modname}/
%{python_sitelib}/%{modname}-%{version}-py*.egg-info

%changelog
