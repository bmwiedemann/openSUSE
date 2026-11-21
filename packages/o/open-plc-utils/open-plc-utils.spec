#
# spec file for package open-plc-utils
#
# Copyright (c) 2026 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). In either case, the license is the
# MIT License.
#
# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           open-plc-utils
Version:        0.0.6~git20260908.5e02957
Release:        0
Summary:        Qualcomm Atheros HomePlug Powerline Toolkit
# tools/getargv.c (ISC) links into pibruin; everything else is BSD-3-Clause.
License:        BSD-3-Clause AND ISC
URL:            https://github.com/qca/open-plc-utils
Source0:        %{name}-%{version}.tar.zst
BuildRequires:  gcc
BuildRequires:  make

%description
Open toolkit for HomePlug 1.0, HomePlug AV and HomePlug AV2 powerline
network adapters with Qualcomm Atheros chipsets: list adapters and link
rates (plcstat), read and manage adapter identity and keys (plctool),
flash firmware and parameter blocks, and more. The tools open raw
Ethernet sockets, so they run as root or with cap_net_raw.

%prep
%setup -q

%build
# make.def appends its defaults to the environment flags, so optflags apply.
export CFLAGS="%{optflags}"
# VisualStudioNET holds Windows-only project files excluded from the source.
%make_build prefix=%{_prefix} mandir=%{_mandir} FOLDERS="ether key mdio mme nodes nvm pib plc ram serial slac tools"

%install
%make_install prefix=%{_prefix} mandir=%{_mandir} FOLDERS="ether key mdio mme nodes nvm pib plc ram serial slac tools" install manuals

# Upstream ships no test suite: the per-directory `check` targets only
# recompile sources standalone, and the tools need raw-socket access to
# physical powerline hardware.

%files
%license LICENSE
%doc README NOTICES
%{_bindir}/ampboot
%{_bindir}/amphost
%{_bindir}/ampID
%{_bindir}/amplist
%{_bindir}/amprate
%{_bindir}/amprule
%{_bindir}/ampstat
%{_bindir}/amptest
%{_bindir}/amptone
%{_bindir}/amptool
%{_bindir}/ampwait
%{_bindir}/chknvm
%{_bindir}/chknvm2
%{_bindir}/chkpib
%{_bindir}/chkpib2
%{_bindir}/CMEncrypt
%{_bindir}/config2cfg
%{_bindir}/coqos_add
%{_bindir}/coqos_info
%{_bindir}/coqos_man
%{_bindir}/coqos_mod
%{_bindir}/coqos_rel
%{_bindir}/edru
%{_bindir}/edsu
%{_bindir}/efbu
%{_bindir}/efeu
%{_bindir}/efru
%{_bindir}/efsu
%{_bindir}/evse
%{_bindir}/getpib
%{_bindir}/hpav
%{_bindir}/hpavkey
%{_bindir}/hpavkeys
%{_bindir}/int64host
%{_bindir}/int6k
%{_bindir}/int6kbaud
%{_bindir}/int6kboot
%{_bindir}/int6kdetect
%{_bindir}/int6keth
%{_bindir}/int6kf
%{_bindir}/int6khost
%{_bindir}/int6kid
%{_bindir}/int6klist
%{_bindir}/int6klog
%{_bindir}/int6kmdio
%{_bindir}/int6kmdio2
%{_bindir}/int6kmod
%{_bindir}/int6krate
%{_bindir}/int6krule
%{_bindir}/int6kstat
%{_bindir}/int6ktest
%{_bindir}/int6ktone
%{_bindir}/int6kuart
%{_bindir}/int6kwait
%{_bindir}/mac2pw
%{_bindir}/mac2pwd
%{_bindir}/mdioblock
%{_bindir}/mdioblock2
%{_bindir}/mdiodump
%{_bindir}/mdiogen
%{_bindir}/mdustats
%{_bindir}/mme
%{_bindir}/modpib
%{_bindir}/nics
%{_bindir}/nvmmerge
%{_bindir}/nvmsplit
%{_bindir}/pev
%{_bindir}/pib2xml
%{_bindir}/pibcomp
%{_bindir}/pibdump
%{_bindir}/pibruin
%{_bindir}/pibrump
%{_bindir}/plcboot
%{_bindir}/plcdevs
%{_bindir}/plcfwd
%{_bindir}/plcget
%{_bindir}/plchost
%{_bindir}/plchostd
%{_bindir}/plchostd2
%{_bindir}/plcID
%{_bindir}/plclist
%{_bindir}/plclog
%{_bindir}/plcmdio16
%{_bindir}/plcmdio32
%{_bindir}/plcotst
%{_bindir}/plcrate
%{_bindir}/plcrule
%{_bindir}/plcset
%{_bindir}/plcstat
%{_bindir}/plctest
%{_bindir}/plctone
%{_bindir}/plctool
%{_bindir}/plcwait
%{_bindir}/psgraph
%{_bindir}/psin
%{_bindir}/pskey
%{_bindir}/psnotch
%{_bindir}/psout
%{_bindir}/ptsctl
%{_bindir}/rkey
%{_bindir}/sada
%{_bindir}/sdram
%{_bindir}/setpib
%{_bindir}/ttycat
%{_bindir}/ttyrecv
%{_bindir}/ttysend
%{_bindir}/ttysig
%{_bindir}/weeder
%{_bindir}/xml2pib
%{_mandir}/man1/ampboot.1%{?ext_man}
%{_mandir}/man1/amphost.1%{?ext_man}
%{_mandir}/man1/ampID.1%{?ext_man}
%{_mandir}/man1/amplist.1%{?ext_man}
%{_mandir}/man1/amprate.1%{?ext_man}
%{_mandir}/man1/amprule.1%{?ext_man}
%{_mandir}/man1/ampstat.1%{?ext_man}
%{_mandir}/man1/amptest.1%{?ext_man}
%{_mandir}/man1/amptone.1%{?ext_man}
%{_mandir}/man1/amptool.1%{?ext_man}
%{_mandir}/man1/ampwait.1%{?ext_man}
%{_mandir}/man1/chknvm.1%{?ext_man}
%{_mandir}/man1/chknvm2.1%{?ext_man}
%{_mandir}/man1/chkpib.1%{?ext_man}
%{_mandir}/man1/chkpib2.1%{?ext_man}
%{_mandir}/man1/CMEncrypt.1%{?ext_man}
%{_mandir}/man1/config2cfg.1%{?ext_man}
%{_mandir}/man1/coqos_add.1%{?ext_man}
%{_mandir}/man1/coqos_info.1%{?ext_man}
%{_mandir}/man1/coqos_man.1%{?ext_man}
%{_mandir}/man1/coqos_mod.1%{?ext_man}
%{_mandir}/man1/coqos_rel.1%{?ext_man}
%{_mandir}/man1/edru.1%{?ext_man}
%{_mandir}/man1/edsu.1%{?ext_man}
%{_mandir}/man1/efbu.1%{?ext_man}
%{_mandir}/man1/efeu.1%{?ext_man}
%{_mandir}/man1/efru.1%{?ext_man}
%{_mandir}/man1/efsu.1%{?ext_man}
%{_mandir}/man1/evse.1%{?ext_man}
%{_mandir}/man1/getpib.1%{?ext_man}
%{_mandir}/man1/hpav.1%{?ext_man}
%{_mandir}/man1/hpavkey.1%{?ext_man}
%{_mandir}/man1/hpavkeys.1%{?ext_man}
%{_mandir}/man1/int64host.1%{?ext_man}
%{_mandir}/man1/int6k.1%{?ext_man}
%{_mandir}/man1/int6kbaud.1%{?ext_man}
%{_mandir}/man1/int6kboot.1%{?ext_man}
%{_mandir}/man1/int6kdetect.1%{?ext_man}
%{_mandir}/man1/int6keth.1%{?ext_man}
%{_mandir}/man1/int6kf.1%{?ext_man}
%{_mandir}/man1/int6khost.1%{?ext_man}
%{_mandir}/man1/int6kid.1%{?ext_man}
%{_mandir}/man1/int6klist.1%{?ext_man}
%{_mandir}/man1/int6klog.1%{?ext_man}
%{_mandir}/man1/int6kmdio.1%{?ext_man}
%{_mandir}/man1/int6kmdio2.1%{?ext_man}
%{_mandir}/man1/int6kmod.1%{?ext_man}
%{_mandir}/man1/int6krate.1%{?ext_man}
%{_mandir}/man1/int6krule.1%{?ext_man}
%{_mandir}/man1/int6kstat.1%{?ext_man}
%{_mandir}/man1/int6ktest.1%{?ext_man}
%{_mandir}/man1/int6ktone.1%{?ext_man}
%{_mandir}/man1/int6kuart.1%{?ext_man}
%{_mandir}/man1/int6kwait.1%{?ext_man}
%{_mandir}/man1/mac2pw.1%{?ext_man}
%{_mandir}/man1/mac2pwd.1%{?ext_man}
%{_mandir}/man1/mdioblock.1%{?ext_man}
%{_mandir}/man1/mdioblock2.1%{?ext_man}
%{_mandir}/man1/mdiodump.1%{?ext_man}
%{_mandir}/man1/mdiogen.1%{?ext_man}
%{_mandir}/man1/mdustats.1%{?ext_man}
%{_mandir}/man1/mme.1%{?ext_man}
%{_mandir}/man1/modpib.1%{?ext_man}
%{_mandir}/man1/nics.1%{?ext_man}
%{_mandir}/man1/nvmmerge.1%{?ext_man}
%{_mandir}/man1/nvmsplit.1%{?ext_man}
%{_mandir}/man1/pcapdevs.1%{?ext_man}
%{_mandir}/man1/pev.1%{?ext_man}
%{_mandir}/man1/pib2xml.1%{?ext_man}
%{_mandir}/man1/pibcomp.1%{?ext_man}
%{_mandir}/man1/pibdump.1%{?ext_man}
%{_mandir}/man1/pibruin.1%{?ext_man}
%{_mandir}/man1/pibrump.1%{?ext_man}
%{_mandir}/man1/plc.1%{?ext_man}
%{_mandir}/man1/plcboot.1%{?ext_man}
%{_mandir}/man1/plcdevs.1%{?ext_man}
%{_mandir}/man1/plcfwd.1%{?ext_man}
%{_mandir}/man1/plcget.1%{?ext_man}
%{_mandir}/man1/plchost.1%{?ext_man}
%{_mandir}/man1/plchostd.1%{?ext_man}
%{_mandir}/man1/plchostd2.1%{?ext_man}
%{_mandir}/man1/plcID.1%{?ext_man}
%{_mandir}/man1/plclist.1%{?ext_man}
%{_mandir}/man1/plclog.1%{?ext_man}
%{_mandir}/man1/plcmdio16.1%{?ext_man}
%{_mandir}/man1/plcmdio32.1%{?ext_man}
%{_mandir}/man1/plcotst.1%{?ext_man}
%{_mandir}/man1/plcrate.1%{?ext_man}
%{_mandir}/man1/plcrule.1%{?ext_man}
%{_mandir}/man1/plcset.1%{?ext_man}
%{_mandir}/man1/plcstat.1%{?ext_man}
%{_mandir}/man1/plctest.1%{?ext_man}
%{_mandir}/man1/plctone.1%{?ext_man}
%{_mandir}/man1/plctool.1%{?ext_man}
%{_mandir}/man1/plcwait.1%{?ext_man}
%{_mandir}/man1/psgraph.1%{?ext_man}
%{_mandir}/man1/psin.1%{?ext_man}
%{_mandir}/man1/pskey.1%{?ext_man}
%{_mandir}/man1/psnotch.1%{?ext_man}
%{_mandir}/man1/psout.1%{?ext_man}
%{_mandir}/man1/ptsctl.1%{?ext_man}
%{_mandir}/man1/rkey.1%{?ext_man}
%{_mandir}/man1/sada.1%{?ext_man}
%{_mandir}/man1/sdram.1%{?ext_man}
%{_mandir}/man1/setpib.1%{?ext_man}
%{_mandir}/man1/ttycat.1%{?ext_man}
%{_mandir}/man1/ttyrecv.1%{?ext_man}
%{_mandir}/man1/ttysend.1%{?ext_man}
%{_mandir}/man1/ttysig.1%{?ext_man}
%{_mandir}/man1/weeder.1%{?ext_man}
%{_mandir}/man1/xml2pib.1%{?ext_man}

%changelog
