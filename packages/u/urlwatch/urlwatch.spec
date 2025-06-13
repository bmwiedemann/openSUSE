#
# spec file for package urlwatch
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


%define pythons python3
Name:           urlwatch
Version:        2.29
Release:        0
Summary:        A tool for monitoring webpages for updates
License:        BSD-3-Clause
Group:          Productivity/Networking/Web/Utilities
URL:            https://thp.io/2008/urlwatch/
Source0:        https://github.com/thp/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel >= 3.8
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
Requires:       python3-PyYAML
Requires:       python3-cssselect
Requires:       python3-keyring
Requires:       python3-lxml
Requires:       python3-minidb >= 2.0.6
Requires:       python3-platformdirs
Requires:       python3-requests
BuildArch:      noarch

%description
urlwatch is intended to help you watch changes in webpages and get
notified (via email, in your terminal or with a custom-written
reporter class) of any changes. The change notification will include
the URL that has changed and a unified diff of what has changed.

A default config is ~/.urlwatch/urlwatch.yaml.
use "urlwatch --edit-config" to customize it.

You need to create ~/.urlwatch/urls.yaml in order to use urlwatch.
Use "urlwatch --edit" to open the file with your editor.

Please look in

 %{_docdir}/urlwatch/README.md

 TIPS AND TRICKS what to use in urls.yaml.

%prep
%setup -q

%build
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}%{python3_sitelib}

%files
%doc CHANGELOG* README*
%license COPYING*
%{_bindir}/%{name}
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}.dist-info
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man5/urlwatch-config.5%{?ext_man}
%{_mandir}/man5/urlwatch-filters.5%{?ext_man}
%{_mandir}/man5/urlwatch-jobs.5%{?ext_man}
%{_mandir}/man5/urlwatch-reporters.5%{?ext_man}
%{_mandir}/man7/urlwatch-cookbook.7%{?ext_man}
%{_mandir}/man7/urlwatch-deprecated.7%{?ext_man}
%{_mandir}/man7/urlwatch-intro.7%{?ext_man}

%changelog
