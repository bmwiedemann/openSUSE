#
# spec file for package newt-doc
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


Name:           newt-doc
Version:        0.52.23
Release:        0
Summary:        Tutorial for Nifty Erik's Windowing Toolkit
License:        LGPL-2.1-or-later
Group:          Documentation/Howto
URL:            https://pagure.io/newt
Source:         https://fedorahosted.org/releases/n/e/newt/newt-%{version}.tar.gz
# needed for tutorial.pdf
BuildRequires:  docbook-toys
BuildRequires:  texlive-courier
BuildRequires:  texlive-dvips
BuildRequires:  texlive-ec
BuildRequires:  texlive-helvetic
BuildRequires:  texlive-jadetex
BuildRequires:  texlive-times
Recommends:     newt = %{version}
BuildArch:      noarch

%description
This package contains a tutorial about the Newt windowing toolkit.

Newt is a programming library for color text-mode, widget-based user
interfaces.  Newt can be used to add stacked windows, entry widgets,
check boxes, radio buttons, labels, plain text fields, scrollbars,
etc., to text mode user interfaces. Newt is based on the slang library.

%prep
%autosetup -p1 -n newt-%{version}

%build
# create tutorial.pdf documentation
db2pdf tutorial.sgml

%install

%files
%defattr(-,root,root)
%doc tutorial.{sgml,pdf,tex}

%changelog
