#
# spec file for package python-mutt-ics
#
# Copyright (c) 2020 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-mutt-ics
Version:        0.9.2
Release:        0
Summary:        A tool to show calendar event details in Mutt
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/dmedvinsky/mutt-ics
Source0:        https://files.pythonhosted.org/packages/source/m/mutt_ics/mutt_ics-%{version}.tar.gz
BuildRequires:  %{python_module icalendar >= 3.9.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-icalendar >= 3.9.0
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%ifpython3
Provides:       mutt-ics
Provides:       mutt_ics
%endif
%python_subpackages

%description
A tool to show calendar event details in Mutt.

%prep
%setup -q -n mutt_ics-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/mutt-ics
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
exit_code=0
%python_exec build/lib/mutt_ics/mutt_ics.py samples/1.ics | grep Subject   || exit_code=1
%python_exec build/lib/mutt_ics/mutt_ics.py samples/2.ics | grep Start     || exit_code=2
%python_exec build/lib/mutt_ics/mutt_ics.py samples/3.ics | grep Organizer || exit_code=3
exit $exit_code

%post
%python_install_alternative mutt-ics

%postun
%python_uninstall_alternative mutt-ics

%files %{python_files}
%doc README.md
%python_alternative %{_bindir}/mutt-ics
%{python_sitelib}/*

%changelog
