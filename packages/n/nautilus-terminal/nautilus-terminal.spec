#
# spec file for package nautilus-terminal
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


Name:           nautilus-terminal
Version:        3.5.0
Release:        0
Summary:        A terminal embedded in Nautilus, the GNOME's file browser
License:        GPL-3.0-only
URL:            https://github.com/flozz/nautilus-terminal
Source:         https://files.pythonhosted.org/packages/source/n/nautilus-terminal/nautilus_terminal-%{version}.tar.gz
BuildRequires:  python3-psutil >= 5.6.6
BuildRequires:  python3-setuptools
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python-nautilus-common-devel
BuildRequires:  pkgconfig(glib-2.0)
Requires:       nautilus
Requires:       python3-psutil >= 5.6.6
BuildArch:      noarch

%description
Nautilus Terminal is an integrated terminal for the Nautilus file browser.

%prep
%setup -q -n nautilus_terminal-%{version}

%build
%python3_build

%install
%python3_install
%fdupes %{buildroot}%{python3_sitelib}

%files
%doc README.rst
%{python3_sitelib}/nautilus_terminal*
%{_datadir}/glib-2.0/schemas/org.flozz.nautilus-terminal.gschema.xml
%{_datadir}/nautilus-python/extensions/nautilus_terminal_extension.py

%changelog
