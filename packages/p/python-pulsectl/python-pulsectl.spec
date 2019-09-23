#
# spec file for package python-pulsectl
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without test
Name:           python-pulsectl
Version:        18.12.5
Release:        0
Summary:        Python high-level interface and ctypes-based bindings for PulseAudio (libpulse)
License:        MIT
Group:          Development/Languages/Python
URL:            http://github.com/mk-fg/python-pulse-control
Source:         https://files.pythonhosted.org/packages/source/p/pulsectl/pulsectl-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       pulseaudio >= 5.0
Requires:       python-setuptools
BuildArch:      noarch
%if %{with test}
BuildRequires:  libpulse-devel >= 5.0
BuildRequires:  pulseaudio
BuildRequires:  pulseaudio-utils
%endif
%python_subpackages

%description
Python (3.x and 2.x) high-level interface and ctypes-based bindings for
PulseAudio (libpulse), mostly focused on mixer-like controls and
introspection-related operations (as opposed to e.g. submitting sound samples to
play, player-like client).

%prep
%setup -q -n pulsectl-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%python_exec -m unittest pulsectl.tests.all
%endif

%files %{python_files}
%license COPYING
%doc CHANGES.rst README.rst
%{python_sitelib}/*

%changelog
