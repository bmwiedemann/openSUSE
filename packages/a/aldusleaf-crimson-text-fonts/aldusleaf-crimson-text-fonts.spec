#
# spec file for package aldusleaf-crimson-text-fonts
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define fontname crimson

Name:           aldusleaf-crimson-text-fonts
Version:        20111206
Release:        0
Summary:        Crimson Text Serif Font
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://aldusleaf.org/
Source0:        %{fontname}_%{version}.zip
Source2:        specimen.pdf
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Crimson Text is a font family for book production in the tradition
of beautiful oldstyle typefaces.
Crimson Text was born after years of discontent with the choice of
free text typefaces. It is a friendly, classical old-style font for books.

%prep
%setup -T -c %{name} -n %{name}
unzip %{SOURCE0}
cp %{SOURCE2} .

%build
# -- nothing to do --

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 444 %{fontname}/*.otf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%defattr(0644,root,root,755)
%doc *.pdf %{fontname}/README
%dir %{_ttfontsdir}
%{_ttfontsdir}/*.otf

%changelog
