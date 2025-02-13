#
# spec file for package python-python-oxmsg
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


%{?sle15_python_module_pythons}
Name:           python-python-oxmsg
Version:        0.0.2
Release:        0
Summary:        Parse Outlook MSG (.msg) files to extract email messages and attachments
License:        MIT
URL:            https://github.com/scanny/python-oxmsg
Source:         %{url}/archive/v%{version}.tar.gz#/python_oxmsg-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.0.0}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module olefile}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing_extensions >= 4.9.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-click
Requires:       python-olefile
Requires:       python-typing_extensions >= 4.9.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
The target use case is extracting Outlook message text and accessing attachments.
There is no support for modifying messages or creating them from scratch. In
addition to message text, other message properties such as sent-date, etc. are
also accessible.

%prep
%autosetup -p1 -n python-oxmsg-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/oxmsg
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative oxmsg

%postun
%python_uninstall_alternative oxmsg

%files %{python_files}
%python_alternative %{_bindir}/oxmsg
%{python_sitelib}/oxmsg
%{python_sitelib}/python_oxmsg-%{version}.dist-info

%changelog
