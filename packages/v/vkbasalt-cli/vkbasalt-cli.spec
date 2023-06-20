#
# spec file for package python-vkbasalt-cli
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
%global appid io.gitlab.theevilskeleton.vkbasalt_cli
%global appname vkbasalt-cli
%global cliname vkbasalt

%define skip_python2 1
%define skip_python39 1
%define skip_python310 1

Name:           vkbasalt-cli
Version:        3.1.1
Release:        0
Summary:        Command-line utility for vkBasalt
License:        LGPL-3.0-only
URL:            https://gitlab.com/TheEvilSkeleton/vkbasalt-cli
Source0:        https://gitlab.com/TheEvilSkeleton/vkbasalt-cli/-/archive/v%{version}/%{appname}-v%{version}.tar.gz  
BuildRequires:  python-rpm-macros
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  fdupes
BuildArch:      noarch

%description
vkbasalt-cli (filename vkbasalt) is a CLI utility and library in conjunction with vkBasalt. This makes generating configuration files or running vkBasalt with games easier. This is mainly convenient in environments where integrating vkBasalt is wishful, for example a GUI application. Integrating vkbasalt-cli allows a front-end to easily generate and use specific configurations on the fly, without asking the user to manually write a configuration file

%prep
%autosetup -n %{appname}-v%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# No tests available, even upstream

%files
%license COPYING
%doc README.md
%{_bindir}/vkbasalt
%{python_sitelib}/vkbasalt
%{python_sitelib}/vkbasalt_cli-%{version}*-info

%changelog
