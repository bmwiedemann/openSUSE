#
# spec file for package libnss_usrfiles
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


Name:           libnss_usrfiles
Version:        2.27
Release:        0
Summary:        NSS usrfiles plugin for glibc
License:        LGPL-2.1-only
Group:          System/Base
URL:            http://github.com/kubic-project/libnss_usrfiles
Source:         %{name}-%{version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  autoconf
BuildRequires:  libtool

%description
The NSS usrfiles plugin additionally looks in /usr/etc for passwd and
group data.

%package -n libnss_usrfiles2
Summary:        NSS usrfiles plugin for glibc
# we need cp
Group:          System/Libraries
Requires(post): coreutils
Requires(post): glibc
Requires(post): sed
Requires(postun): glibc
Requires(postun): sed

%description -n libnss_usrfiles2
The NSS usrfiles plugin looks additional in %{_prefix}%{_sysconfdir} for passwd and
group data.

%prep
%setup -q

%build
%configure --libdir=/%{_lib}
make %{?_smp_mflags}

%install
%make_install
rm -v %{buildroot}/%{_lib}/%{name}.{a,la,so}
mkdir -p %{buildroot}%{_prefix}%{_sysconfdir}

%post -n libnss_usrfiles2
/sbin/ldconfig
if [ "$1" = 1 ] ; then
    cp -a %{_sysconfdir}/nsswitch.conf %{_sysconfdir}/nsswitch.conf.nss_usrfiles
    sed -i -e 's|^passwd: compat$|passwd: files usrfiles|g' -e 's|^group:  compat$|group:  files usrfiles|g' %{_sysconfdir}/nsswitch.conf
    for service in aliases ethers protocols rpc services ; do
	sed -i -e "s|\(^${service}:[[:space:]]\+files\)|\1 usrfiles|g" %{_sysconfdir}/nsswitch.conf
    done
fi

%postun -n libnss_usrfiles2
/sbin/ldconfig
if [ "$1" = 0 ] ; then
    sed -i -e 's|^passwd: files usrfiles$|passwd: compat|g' -e 's|^group:  files usrfiles$|group:  compat|g' %{_sysconfdir}/nsswitch.conf
    for service in aliases ethers protocols rpc services ; do
        sed -i -e "s|usrfiles||g" %{_sysconfdir}/nsswitch.conf
    done
fi

%files -n libnss_usrfiles2
%license COPYING
%doc README.md
/%{_lib}/libnss_usrfiles.so.2*
%dir %{_prefix}%{_sysconfdir}

%changelog
