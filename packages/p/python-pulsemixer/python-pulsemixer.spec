#
# spec file for package python-pulsemixer
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
Name:           python-pulsemixer
Version:        1.5.1
Release:        0
Summary:        pulsemixer - CLI and curses mixer for PulseAudio
License:        MIT
Group:          Productivity/Multimedia/Sound/Mixers
URL:            https://github.com/GeorgeFilipkin/pulsemixer
Source:         https://files.pythonhosted.org/packages/source/p/pulsemixer/pulsemixer-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
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

%pre
%python_libalternatives_reset_alternative pulsemixer

%post
%python_install_alternative pulsemixer

%postun
%python_uninstall_alternative pulsemixer

%files %{python_files}
%doc README.md
%python_alternative %{_bindir}/pulsemixer
%{python_sitelib}/pulsemixer-%{version}.dist-info

%changelog
