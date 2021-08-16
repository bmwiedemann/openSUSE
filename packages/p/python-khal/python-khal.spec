#
# spec file for package python-khal
#
# Copyright (c) 2021 SUSE LLC
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


%define skip_python36 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-khal
Version:        0.10.4
Release:        0
Summary:        CLI calendar with CalDAV support
License:        MIT
Group:          Productivity/Office/Organizers
URL:            https://lostpackets.de/khal/
Source0:        https://files.pythonhosted.org/packages/source/k/khal/khal-%{version}.tar.gz
BuildRequires:  %{python_module atomicwrites >= 0.1.7}
BuildRequires:  %{python_module click >= 3.2}
BuildRequires:  %{python_module click-log >= 0.2.0}
BuildRequires:  %{python_module configobj}
BuildRequires:  %{python_module dateutil}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module icalendar >= 4.0.3}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module pyxdg}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module tzlocal >= 1.0}
BuildRequires:  %{python_module urwid >= 1.3.0}
BuildRequires:  %{python_module vdirsyncer}
BuildRequires:  fdupes
Requires:       python-atomicwrites
Requires:       python-click
Requires:       python-click-log
Requires:       python-configobj
Requires:       python-dateutil
Requires:       python-icalendar
Requires:       python-pytz
Requires:       python-pyxdg
Requires:       python-tzlocal
Requires:       python-urwid
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Khal is a CLI (console), CalDAV based calendar program, allowing syncing of
calendars with a variety of other programs on a host of different platforms.

%prep
%setup -q -n khal-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/khal
%python_clone -a %{buildroot}%{_bindir}/ikhal
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Requires /dev/tty working
# https://github.com/pimutils/khal/issues/683
%pytest -k "not test_import_from_stdin"

%post
%python_install_alternative khal
%python_install_alternative ikhal

%postun
%python_uninstall_alternative khal
%python_uninstall_alternative ikhal

%files %{python_files}
%license COPYING
%doc AUTHORS.txt CONTRIBUTING.rst README.rst khal.conf.sample
%{python_sitelib}/khal*
%python_alternative %{_bindir}/khal
%python_alternative %{_bindir}/ikhal

%changelog
