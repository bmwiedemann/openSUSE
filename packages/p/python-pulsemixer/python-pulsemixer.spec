#
# spec file for package python-pulsemixer
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

Name:           python-pulsemixer
Version:        1.5.1
Release:        0
Summary:        pulsemixer - CLI and curses mixer for PulseAudio
License:        MIT
Group:          Productivity/Multimedia/Sound/Mixers
URL:            https://github.com/GeorgeFilipkin/pulsemixer
Source:         https://files.pythonhosted.org/packages/source/p/pulsemixer/pulsemixer-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
pulsemixer - CLI and curses mixer for PulseAudio

%prep
%autosetup -p1 -n pulsemixer-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pulsemixer
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative pulsemixer

%postun
%python_uninstall_alternative pulsemixer

%files %{python_files}
%doc README.md
%python_alternative %{_bindir}/pulsemixer
%{python_sitelib}/pulsemixer-%{version}.dist-info

%changelog
