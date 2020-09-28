#
# spec file for package buildstream
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


%define real_name BuildStream

Name:           buildstream
Version:        1.6.0
Release:        0
Summary:        A framework for modelling build pipelines in YAML
License:        LGPL-2.1-or-later
Group:          Development/Tools/Building
URL:            https://wiki.gnome.org/Projects/BuildStream
Source0:        https://download.gnome.org/sources/BuildStream/1.6/%{real_name}-%{version}.tar.xz

BuildRequires:  bubblewrap
BuildRequires:  fdupes
BuildRequires:  python3-base >= 3.4
BuildRequires:  python3-devel >= 3.4
BuildRequires:  python3-gobject
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-setuptools
BuildRequires:  typelib-1_0-OSTree-1_0
Requires:       bubblewrap
Requires:       python3-base >= 3.4
Requires:       python3-click
Requires:       python3-gobject
Requires:       python3-psutil
Requires:       python3-ruamel.yaml >= 0.16
Requires:       typelib-1_0-OSTree-1_0

%description
BuildStream is a flexible and extensible framework for the modelling of
build and CI pipelines in a declarative YAML format, written in python.

%prep
%setup -q -n %{real_name}-%{version}
# Fix the shebang
find -type f -exec sed -i 's|%{_bindir}/env python3|%{_bindir}/python3|' {} \;

%build
%python3_build

%install
%python3_install
%fdupes %{buildroot}%{python3_sitelib}

%files
%license COPYING
%doc HACKING.rst MAINTAINERS NEWS README.rst
%{_bindir}/bst
%{_bindir}/bst-artifact-server
%{_datadir}/bash-completion/completions/bst
%{python3_sitelib}/BuildStream-*-py3.?.egg-info
%{python3_sitelib}/buildstream
%{_mandir}/man1/bst*%{ext_man}

%changelog
