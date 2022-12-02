#
# spec file for package scim-sunpinyin
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


Name:           scim-sunpinyin
Version:        2.0.3
Release:        0
Summary:        Sunpinyin module for scim
License:        CDDL-1.0 OR LGPL-2.1-only
Group:          System/I18n/Chinese
URL:            http://code.google.com/p/sunpinyin/
Source:         http://sunpinyin.googlecode.com/files/%{name}-%{version}.tar.gz
#Add GTK_CHECK_VERSION to remove some deprecated functions fjkong@suse.com
Patch1:         scim-sunpinyin-remove-old-functions.patch
#BuildRequires gtk3-devel fjkong@suse.com
Patch2:         scim-sunpinyin-sconstruct-gtk3.patch
# PATCH-FIX-UPSTREAM scim-sunpinyin-scons-on-py3.patch dimstar@opensuse.org -- Fix build with scons using python3 as interpreter
Patch3:         scim-sunpinyin-scons-on-py3.patch
BuildRequires:  gcc-c++
%if 0%{?sles_version}
BuildRequires:  gtk2-devel
%else
BuildRequires:  gtk3-devel
%endif
BuildRequires:  intltool
BuildRequires:  libsunpinyin3
BuildRequires:  python3
BuildRequires:  scim-devel
BuildRequires:  scons
%if 0%{?suse_version}
BuildRequires:  sqlite3-devel
%else
BuildRequires:  sqlite-devel
%endif
BuildRequires:  sunpinyin-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
SunPinyin
===

SunPinyin is an SLM (Statistical Language Model) based input method
engine. To model the Chinese language, it use a backoff bigram and
trigram language model.

Currently, SunPinyin 2.0 is available on IBus.

scim-sunpinyin
===

scim-sunpinyin is a wrapper around SunPinyin which enables user to use
SunPinyin with scim framework.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
scons --prefix=/usr --libdir=%{_libdir}

%install
scons install --prefix=/usr --libdir=%{_libdir} --install-sandbox=%{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/scim-1.0/1.4.0/IMEngine/sunpinyin_imengine.so
%{_libdir}/scim-1.0/1.4.0/SetupUI/sunpinyin_imengine_setup.so
%{_datadir}/scim/icons/sunpinyin_logo.png

%changelog
