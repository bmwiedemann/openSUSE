#
# spec file for package streamdeck-ui
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

%define pythons python3

Name:           streamdeck-ui
Version:        2.0.15
Release:        0
Summary:        Stream Deck tools (service, Web Interface, and UI)
License:        MIT
URL:            https://timothycrosley.github.io/streamdeck-ui/
Source:         https://files.pythonhosted.org/packages/source/s/streamdeck-ui/streamdeck_ui-%{version}.tar.gz
Source1:        70-streamdeck.rules
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
# SECTION test requirements
BuildRequires:  python3-CairoSVG >= 2.5.2
BuildRequires:  python3-filetype >= 1.0.10
BuildRequires:  python3-Pillow >= 9.4.0
BuildRequires:  python3-pynput >= 1.7.6
BuildRequires:  python3-python-xlib >= 0.33
BuildRequires:  python3-pyside6 >= 6.4.2
BuildRequires:  python3-streamdeck >= 0.9.3
# /SECTION
BuildRequires:  fdupes
BuildRequires:	udev
Requires:       python3-CairoSVG >= 2.5.2
Requires:       python3-filetype >= 1.0.10
Requires:       python3-Pillow >= 9.4.0
Requires:       python3-pynput >= 1.7.6
Requires:       python3-pyside6 >= 6.4.2
Requires:       python3-python-xlib >= 0.33
Requires:       python3-streamdeck >= 0.9.3
Requires:       python3-evdev >= 1.3
BuildArch:      noarch

%description
A service, Web Interface, and UI for interacting with your computer using a Stream Deck

%prep
%setup -q -n streamdeck_ui-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

install -D -m0644 %{S:1} %{buildroot}%{_udevrulesdir}/70-streamdeck.rules


%files
%{_bindir}/streamdeck
%{python_sitelib}/streamdeck_ui
%{python_sitelib}/streamdeck_ui-%{version}*-info
%{_udevrulesdir}/70-streamdeck.rules

%changelog
