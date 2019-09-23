#
# spec file for package kdelibs4-apidocs
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           kdelibs4-apidocs
Version:        4.14.38
Release:        0
Summary:        KDE 4 API documentation
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            http://www.kde.org
Source0:        kdelibs-%{version}.tar.xz
Source1:        baselibs.conf
Source2:        hidden.desktop
Source3:        ycp.xml
Source4:        kde4rc
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  graphviz
# seems to be required for png output for graphviz
BuildRequires:  graphviz-gnome
BuildRequires:  kde4-filesystem
BuildRequires:  libqt4-devel-doc
BuildRequires:  xz
Requires:       kde4-filesystem
BuildArch:      noarch

%define debug_package_requires %{name} = %{version}-%{release} libqt4-debuginfo

%description
This package includes the KDE 4 API documentation in HTML
format for easy browsing.

%prep
%setup -q -n kdelibs-%{version}

%build
  export QTDOCDIR=`pkg-config --variable=docdir Qt`
  doc/api/doxygen.sh .

%install
  mkdir -p %{buildroot}%{_kde4_htmldir}/en
  cp -prf kdelibs-%{version}-apidocs %{buildroot}%{_kde4_htmldir}/en/kdelibs4-apidocs
  find %{buildroot} -name installdox | xargs rm -f
  %fdupes %{buildroot}%{_kde4_htmldir}/en/kdelibs4-apidocs
  %kde_post_install

%files
%{_kde4_htmldir}/en/kdelibs4-apidocs/

%changelog
