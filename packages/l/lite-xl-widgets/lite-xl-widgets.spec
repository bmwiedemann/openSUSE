#
# spec file for package lite-xl-widgets
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

%define programname lite-xl
Name:           lite-xl-widgets
Version:        git20221227.a632bfd
Release:        0
Summary:        Widgets for %{programname}
License:        MIT
URL:            https://github.com/lite-xl/lite-xl-widgets
Source0:        %{name}-%{version}.tar.gz
Requires:       lite-xl
BuildArch:      noarch

%description
* A widgets plugin that can be used by plugin writers to more easily implement interactive UI elements.
* The plugin leverages lite-xl View system and provides ready to use components to reduce code duplication
for stuff that most of the time is the same and simplify the process of writing your own GUI controls.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{programname}/widget
mkdir -p %{buildroot}%{_datadir}/%{programname}/widget/examples
mkdir -p %{buildroot}%{_datadir}/%{programname}/widget/fonts
mkdir -p %{buildroot}%{_datadir}/doc/%{name}
# ----
install -D -m644 *.lua %{buildroot}%{_datadir}/%{programname}/widget/
install -D -m644 *.json %{buildroot}%{_datadir}/%{programname}/widget/
install -D -m644 examples/*.lua %{buildroot}%{_datadir}/%{programname}/widget/examples/
install -D -m644 fonts/*.lua %{buildroot}%{_datadir}/%{programname}/widget/fonts
install -D -m644 LICENSE %{buildroot}%{_datadir}/doc/%{name}/LICENSE
install -D -m644 README.md %{buildroot}%{_datadir}/doc/%{name}/README.md

%files
%dir %{_datadir}/%{programname}
%dir %{_datadir}/%{programname}/widget
%dir %{_datadir}/doc/%{name}
%{_datadir}/%{programname}/widget/*
%{_datadir}/doc/%{name}/LICENSE
%{_datadir}/doc/%{name}/README.md

%changelog

