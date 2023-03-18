#
# spec file for package python-gpstime
#
# Copyright (c) 2023 SUSE LLC
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


%define modname gpstime
Name:           python-gpstime
Version:        0.6.2
Release:        0
Summary:        GPS-aware Python datetime module
License:        GPL-3.0-or-later
URL:            https://git.ligo.org/cds/software/gpstime
Source:         https://files.pythonhosted.org/packages/source/g/gpstime/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  timezone
Requires:       python-appdirs
Requires:       python-python-dateutil
Requires:       python-requests
Requires:       timezone
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION Tests
BuildRequires:  %{python_module appdirs}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module requests}
# /SECTION
%python_subpackages

%description
This package provides GPS time conversion utilities, including a
gpstime subclass of the built-in datetime class with the addition of
GPS time parsing and conversion methods.

It also provides a command-line GPS conversion utility that uses the
gpstime module, a rough work-alike to LIGO "tconvert" utility.

%prep
%autosetup -n gpstime-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/gpstime
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest

%post
%python_install_alternative gpstime

%postun
%python_uninstall_alternative gpstime

%files %{python_files}
%doc README.md
%license COPYING COPYING-GPL-3
%python_alternative %{_bindir}/gpstime
%{python_sitelib}/%{modname}/
%{python_sitelib}/%{modname}-%{version}-py%{python_version}.egg-info/

%changelog
