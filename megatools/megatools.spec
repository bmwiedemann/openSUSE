#
# spec file for package megatools
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


# See also http://en.opensuse.org/openSUSE:Specfile_guidelines
Name:           megatools
Version:        1.9.98
Release:        0
Summary:        CLI client for mega.co.nz
License:        GPL-2.0
Group:          Productivity/Networking/File-Sharing
Url:            http://megatools.megous.com
Source0:        http://megatools.megous.com/builds/%{name}-%{version}.tar.gz
Source1:        http://megatools.megous.com/builds/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
BuildRequires:  asciidoc
BuildRequires:  fuse-devel
BuildRequires:  glib2-devel >= 2.32.0
BuildRequires:  libcurl-devel
BuildRequires:  libopenssl-devel
BuildRequires:  pcre-devel
Requires:       curl
Requires:       fuse
Requires:       glib-networking >= 2.32.0
Requires:       openssl

%description	-n %{name}
Megatools allow you to copy individual files as well as entire directory trees
to and from the cloud. You can also perform streaming downloads for example to
preview videos and audio files, without needing to download the entire file.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files -n %{name}
%{_bindir}/mega*
%{_datadir}/doc/%{name}
%{_mandir}/man1/mega*
%{_mandir}/man5/mega*
%{_mandir}/man7/mega*
%exclude %{_datadir}/doc/%{name}/INSTALL
%exclude %{_datadir}/doc/%{name}/TODO

%changelog
