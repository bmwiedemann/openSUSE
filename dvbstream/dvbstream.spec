#
# spec file for package dvbstream
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


Name:           dvbstream
Version:        0.6
Release:        0
Summary:        Broadcasts a DVB Stream over the Network
License:        GPL-2.0+
Group:          Productivity/Networking/Other
Url:            http://www.linuxstb.org/dvbstream/index.shtml
Source:         %{name}-cvs.tar.bz2
Patch0:         %{name}-use-rpmopts
Patch1:         %{name}-include.dif

%description
dvbstream can broadcast either a (subset of a) DVB transport stream or
a DVB program stream over a LAN using the rtp protocol. It attempts to
be compliant with RFCs 1889, 1890, 2038, and 2250. It can also dump the
stream to stdout, for example, for local software decoding when using
DVB cards without a hardware MPEG decoder.

%prep
%setup -q -n dvbstream-cvs
rm -rf TELNET/CVS
%patch0
%patch1 -p1

%build
make %{?_smp_mflags}

%install
bins="dvbstream dumprtp rtpfeed ts_filter"
mkdir -p %{buildroot}%{_prefix}/bin
install -m 755 $bins %{buildroot}%{_prefix}/bin

%files
%doc *.sh TELNET COPYING CHANGES README
%{_bindir}/dvbstream
%{_bindir}/dumprtp
%{_bindir}/rtpfeed
%{_bindir}/ts_filter

%changelog
