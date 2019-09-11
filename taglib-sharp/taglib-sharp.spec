#
# spec file for package taglib-sharp
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


Name:           taglib-sharp
Version:        2.1.0.0
Release:        0
Summary:        Multimedia metadata reading/writing library for popular formats
License:        LGPL-2.1+
Group:          Development/Languages/Mono
Url:            http://download.banshee-project.org/taglib-sharp/
Source0:        http://download.banshee.fm/taglib-sharp/2.1.0.0/%{name}-%{version}.tar.bz2
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gnome-sharp-2.0)
BuildRequires:  pkgconfig(mono)
BuildRequires:  pkgconfig(mono-nunit)

%description
TagLib# is a metadata or "tag" reader and writer library that supports the
most common movie and music formats, abstracting away format specificity.
TagLib# offers either a common API for all formats or access to specific

%package devel
Summary:        Multimedia metadata reading/writing library for popular formats
Group:          Development/Languages/Mono
Requires:       %{name} = %{version}
Requires:       pkgconfig

%description devel
TagLib# is a metadata or "tag" reader and writer library that supports the
most common movie and music formats, abstracting away format specificity.
TagLib# offers either a common API for all formats or access to specific
APIs for a given format.

%prep
%setup -q

%build
%configure                   \
   --libdir=%{_libexecdir}   \
   --disable-docs
make %{?_smp_mflags}

%install
%makeinstall
install -Dm 0644 %{name}.pc %{buildroot}%{_datadir}/pkgconfig/%{name}.pc
find %{buildroot}%{_libexecdir} -name '*.pc' -type f -delete -print

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libexecdir}/mono/gac/
%{_libexecdir}/mono/

%files devel
%defattr(-, root, root)
%{_datadir}/pkgconfig/*.pc

%changelog
