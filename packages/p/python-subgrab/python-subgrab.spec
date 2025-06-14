#
# spec file for package python-subgrab
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


%bcond_without libalternatives
Name:           python-subgrab
Version:        1.0.4
Release:        0
Summary:        Script to download subtitles for media files
License:        GPL-3.0-only
URL:            https://github.com/RafayGhafoor/Subscene-Subtitle-Grabber
Source:         https://files.pythonhosted.org/packages/source/s/subgrab/subgrab-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       alts
Requires:       python-beautifulsoup4
Requires:       python-lxml
Requires:       python-requests
BuildArch:      noarch
%python_subpackages

%description
A script that allows to download subtitles for TV-Series, Anime and Movies from
subscene and other sites.

%prep
%setup -q -n subgrab-%{version}
rm -rf subgrab.egg-info
sed -i 's/bs4/beautifulsoup4/g' setup.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/subgrab
%python_expand %fdupes %{buildroot}/%{$python_sitelib}

%pre
%python_libalternatives_reset_alternative subgrab

%files %{python_files}
%python_alternative %{_bindir}/subgrab
%{python_sitelib}/subgrab
%{python_sitelib}/subgrab-%{version}*-info

%changelog
