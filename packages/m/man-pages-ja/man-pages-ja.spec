#
# spec file for package man-pages-ja
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           man-pages-ja
Version:        20181215
Release:        0
Summary:        LDP Manual Pages (Japanese)
License:        GPL-2.0-only AND BSD-3-Clause AND GFDL-1.1-only AND GFDL-1.2-only AND GFDL-1.3-only
Group:          Documentation/Man
Summary(ja):    Linux 日本語マン・ページ
Url:            http://linuxjm.sourceforge.jp/download.html
Source:         http://linuxjm.sourceforge.jp/man-pages-ja-%{version}.tar.gz
# Some manpages are only shipped if the programs exist..
BuildRequires:  cdparanoia
BuildRequires:  fdupes
Provides:       locale(man:ja)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description -l ja
このパッケージは linux のための日本語のマン・ページを提供するものです。
現在はまだ alpha 配布なので、不十分な点が多々ありますがご了承ください。

%description
These are the Japanese man pages of the Linux Documentation Project.
Note that they are normally older than the English versions.  For
reference, you should use the English versions.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_mandir}/ja
# There are some duplicates.
# Adjust the following list of subdirectories
# so that the preferred versions of the man pages come
# last and thus overwrite the less good versions:
# especially:
# prefer LDP_man-pages over bind
# prefer LDP_man-pages over netkit
# prefer LDP_man-pages over ld.so
# prefer LDP_man-pages over shadow
# prefer gnumaniak over GNU_sh-utils
# prefer gnumaniak over GNU_textutils
# prefer gnumaniak over GNU_sh-utils
# prefer gnumaniak over GNU_fileutils
# prefer man-db over man
# prefer util-linux over SysVinit
# prefer util-linux over shadow
# prefer util-linux over procps
# prefer util-linux over netkit
# prefer nfs-utils over SysVinit
# prefer nfs-utils over nfs-server
# prefer netkit over wu-ftpd
# prefer ypbind over ypbind-mt
for dir in \
    GNU_bash \
    GNU_bc \
    GNU_binutils \
    GNU_cpio \
    GNU_ed \
    GNU_fileutils \
    GNU_findutils \
    GNU_gawk \
    GNU_gcc \
    GNU_gdb \
    GNU_gdbm \
    GNU_grep \
    GNU_groff \
    GNU_gzip \
    GNU_indent \
    GNU_less \
    GNU_make \
    GNU_patch \
    GNU_rcs \
    GNU_screen \
    GNU_sed \
    GNU_sh-utils \
    GNU_sharutils \
    GNU_tar \
    GNU_texinfo \
    GNU_textutils \
    GNU_uucp \
    SysVinit \
    apmd \
    at \
    autofs \
    bind \
    bs \
    bsd-games \
    bsd-games-non-free \
    byacc \
    bzip2 \
    cdparanoia \
    cdrecord \
    cron \
    cvsup \
    dhcp \
    dhcpcd \
    e2compr-ancillary \
    e2fsprogs \
    efax \
    eject \
    expect \
    fdutils \
    fetchmail \
    file \
    flex \
    fort77 \
    glibc-linuxthreads \
    ipchains \
    ipchains-scripts \
    ipfwadm \
    iptables \
    ld.so \
    lilo \
    linux-man9 \
    lpr-linux \
    majordomo \
    man \
    mirrordir \
    modutils \
    mpg123 \
    ncftp \
    ncurses \
    net-tools \
    netatalk \
    nfs-server \
    pciutils \
    pcmcia-cs \
    ppp \
    procinfo \
    procps \
    psmisc \
    quota \
    rdate \
    reiserfsprogs \
    rp-pppoe \
    sendmail \
    setserial \
    shadow \
    sudo \
    sysklogd \
    tcp_wrappers \
    tcpdump \
    tcsh \
    ucd-snmp \
    uudeview \
    wu-ftpd \
    xinetd \
    yp-tools \
    ypbind-mt \
    ypserv \
    LDP_man-pages \
    gnumaniak \
    man-db \
    nfs-utils \
    netkit \
    util-linux \
    ypbind \
    zebedee
do
	for i in `find ./manual/$dir/ -regex ".*/man./.+\.."`
	do
	    SUB_DIR=`dirname $i`
	    SUB_DIR=${SUB_DIR##*/}
	    mkdir -p %{buildroot}%{_mandir}/ja/$SUB_DIR
	    install -m 644 $i %{buildroot}%{_mandir}/ja/$SUB_DIR
	done
done
cd %{buildroot}%{_mandir}/ja
for i in */* ; do
    if [ -e %{_mandir}/ja/$i ] || [ -e %{_mandir}/ja/$i.gz ] ; then
	echo %{_mandir}/ja/$i already exists. Deleting it.
        rm -f $i
    fi
done
%fdupes -s %{buildroot}/%{_prefix}

%files
%defattr(-,root,root)
%{_mandir}/ja
%doc README

%changelog
