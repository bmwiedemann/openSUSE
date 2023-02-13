#
# spec file for package words
#
# Copyright (c) 2023 SUSE LLC
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


Name:           words
Version:        2020.12.07
Release:        0
Summary:        An English words dictionary
License:        SUSE-Public-Domain
Group:          Productivity/Office/Dictionary
URL:            http://wordlist.sourceforge.net/
Source0:        https://prdownloads.sourceforge.net/wordlist/scowl-%{version}.tar.gz
Source1:        sysconfig.words
Source2:        SuSEconfig.words
BuildRequires:  glibc-locale
PreReq:         %fillup_prereq
Provides:       scowl = %{version}-%{release}
BuildArch:      noarch

%description
This package contains an English words dictionary which will be installed as

/usr/share/dict/american and linked to /usr/share/dict/words

The symbolic link may be used by look(1) and ispell(1).

For a British or Canadian version of such a words dictionary you may install
words-british or words-canadian respectively.

%package -n words-british
Summary:        A British words dictionary
Group:          Productivity/Text/Utilities
Requires:       words

%description -n words-british
This package contains a British words dictionary which will be installed as

/usr/share/dict/british

For a description see the package words.

%package -n words-canadian
Summary:        A Canadian words dictionary
Group:          Productivity/Text/Utilities
Requires:       words

%description -n words-canadian
This package contains a Canadian words dictionary which will be installed as

/usr/share/dict/canadian

For a description see the package words.

%prep
%setup -q -n scowl-%{version}

%build
spellings="american british canadian"
LANG=POSIX
export POSIX
set +o posix
#
# Do resorting for look(1) command
#
test -d result/ || mkdir result
chmod u+x mk-list
for s in $spellings
do
    case "$s" in
    american*) LC_CTYPE=en_US.UTF-8 ;;
    british*)  LC_CTYPE=en_GB.UTF-8 ;;
    canadian*) LC_CTYPE=en_CA.UTF-8 ;;
    esac
    LC_COLLATE=$LC_CTYPE
    export LC_CTYPE LC_COLLATE
    > result/${s}.todo
    #
    # Fix sorting as the look(1) command expect sort option -f
    # and -d. also convert Latin-1 umlauts into UTF-8 based.
    #
    ./mk-list -v2 ${s} 80 | iconv -f latin1 -t utf8 > >(sort -fdu -S10M -o result/${s} ; rm result/${s}.todo)
done
#
# Wait on sorting FIFOs
#
for s in $spellings
do
    while test -e result/${s}.todo
    do
	sleep 0.05s
    done
done

%install
mkdir -p %{buildroot}%{_datadir}/dict
install -pm 0644 result/* %{buildroot}%{_datadir}/dict/
mkdir -p %{buildroot}%{_localstatedir}/lib/dict
ln -sf ../../..%{_datadir}/dict/american %{buildroot}%{_localstatedir}/lib/dict/words
ln -sf ../../../var/lib/dict/words %{buildroot}%{_datadir}/dict/words
mkdir -p %{buildroot}%{_libexecdir}/words
mkdir -p %{buildroot}%{_fillupdir}
install -pm 0644 %{SOURCE1} %{buildroot}%{_fillupdir}/
install -pm 0755 %{SOURCE2} %{buildroot}%{_libexecdir}/words/update

%post
%{fillup_only}
if test -x %{_libexecdir}/words/update ; then
    %{_libexecdir}/words/update
fi

%preun
test -L usr/share/dict/words && rm usr/share/dict/words || true

%files
%doc Copyright README
%dir %{_libexecdir}/words
%attr(755,root,root) %{_libexecdir}/words/update
%{_datadir}/dict/american
%ghost %{_datadir}/dict/words
%{_fillupdir}/sysconfig.words
%dir %{_localstatedir}/lib/dict/
%verify(not link mtime) %{_localstatedir}/lib/dict/words

%files -n words-british
%{_datadir}/dict/british

%files -n words-canadian
%{_datadir}/dict/canadian

%changelog
