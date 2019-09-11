#
# spec file for package docbook-tdg
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           docbook-tdg
Summary:        DocBook: The Definitive Guide
Version:        2.0.6
Release:        379
Group:          Documentation/Other
BuildRequires:  unzip
License:        GFDL-1.1
Url:            http://docbook.org/tdg/
Source0:        http://docbook.org/tdg/en/tdg-partI-en-2.0.6.pdf
Source1:        http://docbook.org/tdg/en/tdg-partII-en-2.0.6.pdf
Source2:        http://docbook.org/tdg/en/tdg-partIII-en-2.0.6.pdf
Source3:        http://docbook.org/tdg/en/tdg-en-html-2.0.6.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This book is designed to be the clear, concise, normative reference to
the DocBook DTD. This book is the official documentation for the
DocBook DTD.  For printed copies, visit http://docbook.org/tdg/en/.

"Fairly crude PDF versions" (Norman Walsh) of Part I, Part II, and Part
III are included in this package.

%define INSTALL install -m755 -s
%define INSTALL_SCRIPT install -m755
%define INSTALL_DIR install -d -m755
%define INSTALL_DATA install -m644

%prep
%setup -q -T -c
unzip -q %{S:3}
cp %{S:0} %{S:1} %{S:2} .

%build

%install

%files
%defattr(-, root, root)
%doc *.pdf
%doc tdg/en/html
%doc tdg/en/glyphs

%changelog
