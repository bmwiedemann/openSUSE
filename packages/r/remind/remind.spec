#
# spec file for package remind
#
# Copyright (c) 2024 SUSE LLC
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


Name:           remind
Version:        5.1.1
Release:        0
%define tar_version 05.01.01
Summary:        A sophisticated calendar and alarm program
License:        GPL-2.0-only
Group:          Productivity/Office/Organizers
URL:            https://dianne.skoll.ca/projects/remind/
Source0:        %{name}-%{tar_version}.tar.gz
Source100:      %{name}-rpmlintrc
BuildRequires:  perl
BuildRequires:  perl-Cairo
BuildRequires:  perl-Getopt-Long-Descriptive
BuildRequires:  perl-JSON-MaybeXS
BuildRequires:  perl-Pango

Requires:       perl
Requires:       perl-Cairo
Requires:       perl-Getopt-Long-Descriptive
Requires:       perl-JSON-Any
Requires:       perl-Pango
Requires:       tcllib

%description
Remind is a sophisticated calendar and alarm program.
It includes the following features:

* A sophisticated scripting language and intelligent
  handling of exceptions and holidays.
* Plain-text, PostScript and HTML output.
* Timed reminders and pop-up alarms.
* A friendly graphical front-end for people who don't
  want to learn the scripting language.
* Facilities for both the Gregorian and Hebrew calendars.
* Support for 12 different languages.

%prep
%setup -q -n %{name}-%{tar_version}

%build
CFLAGS="%{optflags}" ./configure --disable-perl-build-artifacts --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

##%%check
##make test

%files
%defattr(-,root,root,-)
%doc %{_mandir}/man1/rem.1%{ext_man}
%doc %{_mandir}/man1/rem2html.1%{ext_man}
%doc %{_mandir}/man1/rem2ps.1%{ext_man}
%doc %{_mandir}/man1/rem2pdf.1%{ext_man}
%doc %{_mandir}/man1/remind.1%{ext_man}
%doc %{_mandir}/man1/tkremind.1%{ext_man}
%doc %{_mandir}/man3/Remind::PDF.3pm%{ext_man}
%doc %{_mandir}/man3/Remind::PDF::Entry.3pm%{ext_man}

%{_bindir}/rem
%attr(0755,root,root) %{_bindir}/rem2html
%attr(0755,root,root) %{_bindir}/rem2pdf
%attr(0755,root,root) %{_bindir}/rem2ps
%attr(0755,root,root) %{_bindir}/remind
%attr(0755,root,root) %{_bindir}/tkremind
%attr(0755,root,root) %{perl_vendorlib}/Remind/

%dir /usr/share/remind/
%dir /usr/share/remind/holidays
%dir /usr/share/remind/lang
%dir /usr/share/remind/site
/usr/share/remind/ansitext.rem

/usr/share/remind/holidays/README
/usr/share/remind/holidays/ad.rem
%dir /usr/share/remind/holidays/ad
/usr/share/remind/holidays/ad/02.rem
/usr/share/remind/holidays/ad/03.rem
/usr/share/remind/holidays/ad/04.rem
/usr/share/remind/holidays/ad/05.rem
/usr/share/remind/holidays/ad/06.rem
/usr/share/remind/holidays/ad/07.rem
/usr/share/remind/holidays/ad/08.rem
/usr/share/remind/holidays/ae.rem
/usr/share/remind/holidays/al.rem
/usr/share/remind/holidays/am.rem
/usr/share/remind/holidays/ao.rem
/usr/share/remind/holidays/ar.rem
/usr/share/remind/holidays/as.rem
/usr/share/remind/holidays/at.rem
%dir /usr/share/remind/holidays/at
/usr/share/remind/holidays/at/1.rem
/usr/share/remind/holidays/at/2.rem
/usr/share/remind/holidays/at/3.rem
/usr/share/remind/holidays/at/4.rem
/usr/share/remind/holidays/at/5.rem
/usr/share/remind/holidays/at/6.rem
/usr/share/remind/holidays/at/7.rem
/usr/share/remind/holidays/at/8.rem
/usr/share/remind/holidays/at/9.rem
/usr/share/remind/holidays/au.rem
%dir /usr/share/remind/holidays/au
/usr/share/remind/holidays/au/act.rem
/usr/share/remind/holidays/au/nsw.rem
/usr/share/remind/holidays/au/nt.rem
/usr/share/remind/holidays/au/qld.rem
/usr/share/remind/holidays/au/sa.rem
/usr/share/remind/holidays/au/tas.rem
/usr/share/remind/holidays/au/vic.rem
/usr/share/remind/holidays/au/wa.rem
/usr/share/remind/holidays/aw.rem
/usr/share/remind/holidays/az.rem
/usr/share/remind/holidays/ba.rem
%dir /usr/share/remind/holidays/ba
/usr/share/remind/holidays/ba/bih.rem
/usr/share/remind/holidays/ba/brc.rem
/usr/share/remind/holidays/ba/srp.rem
/usr/share/remind/holidays/bb.rem
/usr/share/remind/holidays/bd.rem
/usr/share/remind/holidays/be.rem
/usr/share/remind/holidays/bf.rem
/usr/share/remind/holidays/bg.rem
/usr/share/remind/holidays/bh.rem
/usr/share/remind/holidays/bi.rem
/usr/share/remind/holidays/bn.rem
/usr/share/remind/holidays/bo.rem
%dir /usr/share/remind/holidays/bo
/usr/share/remind/holidays/bo/b.rem
/usr/share/remind/holidays/bo/c.rem
/usr/share/remind/holidays/bo/h.rem
/usr/share/remind/holidays/bo/l.rem
/usr/share/remind/holidays/bo/n.rem
/usr/share/remind/holidays/bo/o.rem
/usr/share/remind/holidays/bo/p.rem
/usr/share/remind/holidays/bo/s.rem
/usr/share/remind/holidays/bo/t.rem
/usr/share/remind/holidays/br.rem
%dir /usr/share/remind/holidays/br
/usr/share/remind/holidays/br/ac.rem
/usr/share/remind/holidays/br/al.rem
/usr/share/remind/holidays/br/am.rem
/usr/share/remind/holidays/br/ap.rem
/usr/share/remind/holidays/br/ba.rem
/usr/share/remind/holidays/br/ce.rem
/usr/share/remind/holidays/br/df.rem
/usr/share/remind/holidays/br/es.rem
/usr/share/remind/holidays/br/go.rem
/usr/share/remind/holidays/br/ma.rem
/usr/share/remind/holidays/br/mg.rem
/usr/share/remind/holidays/br/ms.rem
/usr/share/remind/holidays/br/pa.rem
/usr/share/remind/holidays/br/pb.rem
/usr/share/remind/holidays/br/pe.rem
/usr/share/remind/holidays/br/pi.rem
/usr/share/remind/holidays/br/pr.rem
/usr/share/remind/holidays/br/rj.rem
/usr/share/remind/holidays/br/rn.rem
/usr/share/remind/holidays/br/ro.rem
/usr/share/remind/holidays/br/rr.rem
/usr/share/remind/holidays/br/rs.rem
/usr/share/remind/holidays/br/sc.rem
/usr/share/remind/holidays/br/se.rem
/usr/share/remind/holidays/br/sp.rem
/usr/share/remind/holidays/br/to.rem
/usr/share/remind/holidays/bs.rem
/usr/share/remind/holidays/bw.rem
/usr/share/remind/holidays/by.rem
/usr/share/remind/holidays/bz.rem
/usr/share/remind/holidays/ca.rem
%dir /usr/share/remind/holidays/ca
/usr/share/remind/holidays/ca/ab.rem
/usr/share/remind/holidays/ca/bc.rem
/usr/share/remind/holidays/ca/mb.rem
/usr/share/remind/holidays/ca/nb.rem
/usr/share/remind/holidays/ca/nl.rem
/usr/share/remind/holidays/ca/ns.rem
/usr/share/remind/holidays/ca/nt.rem
/usr/share/remind/holidays/ca/nu.rem
/usr/share/remind/holidays/ca/on.rem
/usr/share/remind/holidays/ca/pe.rem
/usr/share/remind/holidays/ca/qc.rem
/usr/share/remind/holidays/ca/sk.rem
/usr/share/remind/holidays/ca/yt.rem
/usr/share/remind/holidays/cg.rem
/usr/share/remind/holidays/ch.rem
%dir /usr/share/remind/holidays/ch
/usr/share/remind/holidays/chinese-new-year.rem
/usr/share/remind/holidays/ch/ag.rem
/usr/share/remind/holidays/ch/ai.rem
/usr/share/remind/holidays/ch/ar.rem
/usr/share/remind/holidays/ch/be.rem
/usr/share/remind/holidays/ch/bl.rem
/usr/share/remind/holidays/ch/bs.rem
/usr/share/remind/holidays/ch/fr.rem
/usr/share/remind/holidays/ch/ge.rem
/usr/share/remind/holidays/ch/gl.rem
/usr/share/remind/holidays/ch/gr.rem
/usr/share/remind/holidays/ch/ju.rem
/usr/share/remind/holidays/ch/lu.rem
/usr/share/remind/holidays/ch/ne.rem
/usr/share/remind/holidays/ch/nw.rem
/usr/share/remind/holidays/ch/ow.rem
/usr/share/remind/holidays/ch/sg.rem
/usr/share/remind/holidays/ch/sh.rem
/usr/share/remind/holidays/ch/so.rem
/usr/share/remind/holidays/ch/sz.rem
/usr/share/remind/holidays/ch/tg.rem
/usr/share/remind/holidays/ch/ti.rem
/usr/share/remind/holidays/ch/ur.rem
/usr/share/remind/holidays/ch/vd.rem
/usr/share/remind/holidays/ch/vs.rem
/usr/share/remind/holidays/ch/zg.rem
/usr/share/remind/holidays/ch/zh.rem
/usr/share/remind/holidays/cl.rem
%dir /usr/share/remind/holidays/cl
/usr/share/remind/holidays/cl/ap.rem
/usr/share/remind/holidays/cl/nb.rem
/usr/share/remind/holidays/cm.rem
/usr/share/remind/holidays/co.rem
/usr/share/remind/holidays/cr.rem
/usr/share/remind/holidays/cu.rem
/usr/share/remind/holidays/cw.rem
/usr/share/remind/holidays/cy.rem
/usr/share/remind/holidays/cz.rem
/usr/share/remind/holidays/de.rem
%dir /usr/share/remind/holidays/de
/usr/share/remind/holidays/de/bb.rem
/usr/share/remind/holidays/de/be.rem
/usr/share/remind/holidays/de/bw.rem
/usr/share/remind/holidays/de/by.rem
/usr/share/remind/holidays/de/hb.rem
/usr/share/remind/holidays/de/he.rem
/usr/share/remind/holidays/de/hh.rem
/usr/share/remind/holidays/de/mv.rem
/usr/share/remind/holidays/de/ni.rem
/usr/share/remind/holidays/de/nw.rem
/usr/share/remind/holidays/de/rp.rem
/usr/share/remind/holidays/de/sh.rem
/usr/share/remind/holidays/de/sl.rem
/usr/share/remind/holidays/de/sn.rem
/usr/share/remind/holidays/de/st.rem
/usr/share/remind/holidays/de/th.rem
/usr/share/remind/holidays/discordian.rem
/usr/share/remind/holidays/dj.rem
/usr/share/remind/holidays/dk.rem
/usr/share/remind/holidays/dm.rem
/usr/share/remind/holidays/do.rem
/usr/share/remind/holidays/dz.rem
/usr/share/remind/holidays/ec.rem
/usr/share/remind/holidays/ee.rem
/usr/share/remind/holidays/eg.rem
/usr/share/remind/holidays/es.rem
%dir /usr/share/remind/holidays/es
/usr/share/remind/holidays/es/an.rem
/usr/share/remind/holidays/es/ar.rem
/usr/share/remind/holidays/es/as.rem
/usr/share/remind/holidays/es/cb.rem
/usr/share/remind/holidays/es/ce.rem
/usr/share/remind/holidays/es/cl.rem
/usr/share/remind/holidays/es/cm.rem
/usr/share/remind/holidays/es/cn.rem
/usr/share/remind/holidays/es/ct.rem
/usr/share/remind/holidays/es/ex.rem
/usr/share/remind/holidays/es/ga.rem
/usr/share/remind/holidays/es/ib.rem
/usr/share/remind/holidays/es/mc.rem
/usr/share/remind/holidays/es/md.rem
/usr/share/remind/holidays/es/ml.rem
/usr/share/remind/holidays/es/nc.rem
/usr/share/remind/holidays/es/pv.rem
/usr/share/remind/holidays/es/ri.rem
/usr/share/remind/holidays/es/vc.rem
/usr/share/remind/holidays/et.rem
/usr/share/remind/holidays/fi.rem
/usr/share/remind/holidays/fr.rem
%dir /usr/share/remind/holidays/fr
/usr/share/remind/holidays/fr/bl.rem
/usr/share/remind/holidays/fr/ges.rem
/usr/share/remind/holidays/fr/gp.rem
/usr/share/remind/holidays/fr/gy.rem
/usr/share/remind/holidays/fr/mf.rem
/usr/share/remind/holidays/fr/mq.rem
/usr/share/remind/holidays/fr/nc.rem
/usr/share/remind/holidays/fr/pf.rem
/usr/share/remind/holidays/fr/re.rem
/usr/share/remind/holidays/fr/wf.rem
/usr/share/remind/holidays/fr/yt.rem
/usr/share/remind/holidays/ga.rem
/usr/share/remind/holidays/gb.rem
%dir /usr/share/remind/holidays/gb
/usr/share/remind/holidays/gb/eng.rem
/usr/share/remind/holidays/gb/nir.rem
/usr/share/remind/holidays/gb/sct.rem
/usr/share/remind/holidays/gb/wls.rem
/usr/share/remind/holidays/ge.rem
/usr/share/remind/holidays/gh.rem
/usr/share/remind/holidays/gl.rem
/usr/share/remind/holidays/gr.rem
/usr/share/remind/holidays/gt.rem
/usr/share/remind/holidays/gu.rem
/usr/share/remind/holidays/hk.rem
/usr/share/remind/holidays/hn.rem
/usr/share/remind/holidays/hr.rem
/usr/share/remind/holidays/ht.rem
/usr/share/remind/holidays/hu.rem
/usr/share/remind/holidays/id.rem
/usr/share/remind/holidays/ie.rem
/usr/share/remind/holidays/im.rem
/usr/share/remind/holidays/in.rem
%dir /usr/share/remind/holidays/in
/usr/share/remind/holidays/in/ap.rem
/usr/share/remind/holidays/in/as.rem
/usr/share/remind/holidays/in/br.rem
/usr/share/remind/holidays/in/cg.rem
/usr/share/remind/holidays/in/gj.rem
/usr/share/remind/holidays/in/hr.rem
/usr/share/remind/holidays/in/ka.rem
/usr/share/remind/holidays/in/kl.rem
/usr/share/remind/holidays/in/mh.rem
/usr/share/remind/holidays/in/mp.rem
/usr/share/remind/holidays/in/od.rem
/usr/share/remind/holidays/in/rj.rem
/usr/share/remind/holidays/in/sk.rem
/usr/share/remind/holidays/in/tn.rem
/usr/share/remind/holidays/in/ts.rem
/usr/share/remind/holidays/in/uk.rem
/usr/share/remind/holidays/in/up.rem
/usr/share/remind/holidays/in/wb.rem
/usr/share/remind/holidays/is.rem
/usr/share/remind/holidays/it.rem
%dir /usr/share/remind/holidays/it
/usr/share/remind/holidays/it/ag.rem
/usr/share/remind/holidays/it/al.rem
/usr/share/remind/holidays/it/an.rem
/usr/share/remind/holidays/it/andria.rem
/usr/share/remind/holidays/it/ao.rem
/usr/share/remind/holidays/it/ap.rem
/usr/share/remind/holidays/it/aq.rem
/usr/share/remind/holidays/it/ar.rem
/usr/share/remind/holidays/it/at.rem
/usr/share/remind/holidays/it/av.rem
/usr/share/remind/holidays/it/ba.rem
/usr/share/remind/holidays/it/barletta.rem
/usr/share/remind/holidays/it/bg.rem
/usr/share/remind/holidays/it/bl.rem
/usr/share/remind/holidays/it/bn.rem
/usr/share/remind/holidays/it/bo.rem
/usr/share/remind/holidays/it/br.rem
/usr/share/remind/holidays/it/bs.rem
/usr/share/remind/holidays/it/bt.rem
/usr/share/remind/holidays/it/bz.rem
/usr/share/remind/holidays/it/ca.rem
/usr/share/remind/holidays/it/cb.rem
/usr/share/remind/holidays/it/ce.rem
/usr/share/remind/holidays/it/cesena.rem
/usr/share/remind/holidays/it/ch.rem
/usr/share/remind/holidays/it/cl.rem
/usr/share/remind/holidays/it/cn.rem
/usr/share/remind/holidays/it/co.rem
/usr/share/remind/holidays/it/cr.rem
/usr/share/remind/holidays/it/cs.rem
/usr/share/remind/holidays/it/ct.rem
/usr/share/remind/holidays/it/cz.rem
/usr/share/remind/holidays/it/en.rem
/usr/share/remind/holidays/it/fc.rem
/usr/share/remind/holidays/it/fe.rem
/usr/share/remind/holidays/it/fg.rem
/usr/share/remind/holidays/it/fi.rem
/usr/share/remind/holidays/it/fm.rem
/usr/share/remind/holidays/it/forli.rem
/usr/share/remind/holidays/it/fr.rem
/usr/share/remind/holidays/it/ge.rem
/usr/share/remind/holidays/it/go.rem
/usr/share/remind/holidays/it/gr.rem
/usr/share/remind/holidays/it/im.rem
/usr/share/remind/holidays/it/is.rem
/usr/share/remind/holidays/it/kr.rem
/usr/share/remind/holidays/it/lc.rem
/usr/share/remind/holidays/it/le.rem
/usr/share/remind/holidays/it/li.rem
/usr/share/remind/holidays/it/lo.rem
/usr/share/remind/holidays/it/lt.rem
/usr/share/remind/holidays/it/lu.rem
/usr/share/remind/holidays/it/mb.rem
/usr/share/remind/holidays/it/mc.rem
/usr/share/remind/holidays/it/me.rem
/usr/share/remind/holidays/it/mi.rem
/usr/share/remind/holidays/it/mn.rem
/usr/share/remind/holidays/it/mo.rem
/usr/share/remind/holidays/it/ms.rem
/usr/share/remind/holidays/it/mt.rem
/usr/share/remind/holidays/it/na.rem
/usr/share/remind/holidays/it/no.rem
/usr/share/remind/holidays/it/nu.rem
/usr/share/remind/holidays/it/or.rem
/usr/share/remind/holidays/it/pa.rem
/usr/share/remind/holidays/it/pc.rem
/usr/share/remind/holidays/it/pd.rem
/usr/share/remind/holidays/it/pe.rem
/usr/share/remind/holidays/it/pesaro.rem
/usr/share/remind/holidays/it/pg.rem
/usr/share/remind/holidays/it/pi.rem
/usr/share/remind/holidays/it/pn.rem
/usr/share/remind/holidays/it/pr.rem
/usr/share/remind/holidays/it/pt.rem
/usr/share/remind/holidays/it/pu.rem
/usr/share/remind/holidays/it/pv.rem
/usr/share/remind/holidays/it/pz.rem
/usr/share/remind/holidays/it/ra.rem
/usr/share/remind/holidays/it/rc.rem
/usr/share/remind/holidays/it/re.rem
/usr/share/remind/holidays/it/rg.rem
/usr/share/remind/holidays/it/ri.rem
/usr/share/remind/holidays/it/rm.rem
/usr/share/remind/holidays/it/rn.rem
/usr/share/remind/holidays/it/ro.rem
/usr/share/remind/holidays/it/sa.rem
/usr/share/remind/holidays/it/si.rem
/usr/share/remind/holidays/it/so.rem
/usr/share/remind/holidays/it/sp.rem
/usr/share/remind/holidays/it/sr.rem
/usr/share/remind/holidays/it/ss.rem
/usr/share/remind/holidays/it/su.rem
/usr/share/remind/holidays/it/sv.rem
/usr/share/remind/holidays/it/ta.rem
/usr/share/remind/holidays/it/te.rem
/usr/share/remind/holidays/it/tn.rem
/usr/share/remind/holidays/it/to.rem
/usr/share/remind/holidays/it/tp.rem
/usr/share/remind/holidays/it/tr.rem
/usr/share/remind/holidays/it/trani.rem
/usr/share/remind/holidays/it/ts.rem
/usr/share/remind/holidays/it/tv.rem
/usr/share/remind/holidays/it/ud.rem
/usr/share/remind/holidays/it/urbino.rem
/usr/share/remind/holidays/it/va.rem
/usr/share/remind/holidays/it/vb.rem
/usr/share/remind/holidays/it/vc.rem
/usr/share/remind/holidays/it/ve.rem
/usr/share/remind/holidays/it/vi.rem
/usr/share/remind/holidays/it/vr.rem
/usr/share/remind/holidays/it/vt.rem
/usr/share/remind/holidays/it/vv.rem
/usr/share/remind/holidays/je.rem
/usr/share/remind/holidays/jewish.rem
/usr/share/remind/holidays/jm.rem
/usr/share/remind/holidays/jo.rem
/usr/share/remind/holidays/jp.rem
/usr/share/remind/holidays/ke.rem
/usr/share/remind/holidays/kg.rem
/usr/share/remind/holidays/kh.rem
/usr/share/remind/holidays/kn.rem
/usr/share/remind/holidays/kr.rem
/usr/share/remind/holidays/kw.rem
/usr/share/remind/holidays/kz.rem
/usr/share/remind/holidays/la.rem
/usr/share/remind/holidays/li.rem
/usr/share/remind/holidays/ls.rem
/usr/share/remind/holidays/lt.rem
/usr/share/remind/holidays/lu.rem
/usr/share/remind/holidays/lv.rem
/usr/share/remind/holidays/ma.rem
/usr/share/remind/holidays/mc.rem
/usr/share/remind/holidays/md.rem
/usr/share/remind/holidays/me.rem
/usr/share/remind/holidays/mg.rem
/usr/share/remind/holidays/mh.rem
/usr/share/remind/holidays/mk.rem
/usr/share/remind/holidays/mp.rem
/usr/share/remind/holidays/mr.rem
/usr/share/remind/holidays/mt.rem
/usr/share/remind/holidays/mv.rem
/usr/share/remind/holidays/mw.rem
/usr/share/remind/holidays/mx.rem
/usr/share/remind/holidays/my.rem
%dir /usr/share/remind/holidays/my
/usr/share/remind/holidays/my/01.rem
/usr/share/remind/holidays/my/02.rem
/usr/share/remind/holidays/my/03.rem
/usr/share/remind/holidays/my/04.rem
/usr/share/remind/holidays/my/05.rem
/usr/share/remind/holidays/my/06.rem
/usr/share/remind/holidays/my/07.rem
/usr/share/remind/holidays/my/08.rem
/usr/share/remind/holidays/my/09.rem
/usr/share/remind/holidays/my/10.rem
/usr/share/remind/holidays/my/11.rem
/usr/share/remind/holidays/my/12.rem
/usr/share/remind/holidays/my/13.rem
/usr/share/remind/holidays/my/14.rem
/usr/share/remind/holidays/my/15.rem
/usr/share/remind/holidays/my/16.rem
/usr/share/remind/holidays/mz.rem
/usr/share/remind/holidays/na.rem
/usr/share/remind/holidays/ng.rem
/usr/share/remind/holidays/ni.rem
%dir /usr/share/remind/holidays/ni
/usr/share/remind/holidays/ni/mn.rem
/usr/share/remind/holidays/nl.rem
/usr/share/remind/holidays/no.rem
/usr/share/remind/holidays/nz.rem
%dir /usr/share/remind/holidays/nz
/usr/share/remind/holidays/nz/auk.rem
/usr/share/remind/holidays/nz/can.rem
/usr/share/remind/holidays/nz/cit.rem
/usr/share/remind/holidays/nz/hkb.rem
/usr/share/remind/holidays/nz/mbh.rem
/usr/share/remind/holidays/nz/nsn.rem
/usr/share/remind/holidays/nz/ntl.rem
/usr/share/remind/holidays/nz/ota.rem
/usr/share/remind/holidays/nz/south_canterbury.rem
/usr/share/remind/holidays/nz/stl.rem
/usr/share/remind/holidays/nz/tki.rem
/usr/share/remind/holidays/nz/wgn.rem
/usr/share/remind/holidays/nz/wtc.rem
/usr/share/remind/holidays/pa.rem
/usr/share/remind/holidays/pagan.rem
/usr/share/remind/holidays/pe.rem
/usr/share/remind/holidays/pg.rem
/usr/share/remind/holidays/ph.rem
/usr/share/remind/holidays/pk.rem
/usr/share/remind/holidays/pl.rem
/usr/share/remind/holidays/pr.rem
/usr/share/remind/holidays/pt.rem
%dir /usr/share/remind/holidays/pt
/usr/share/remind/holidays/pt/01.rem
/usr/share/remind/holidays/pt/02.rem
/usr/share/remind/holidays/pt/03.rem
/usr/share/remind/holidays/pt/04.rem
/usr/share/remind/holidays/pt/05.rem
/usr/share/remind/holidays/pt/06.rem
/usr/share/remind/holidays/pt/07.rem
/usr/share/remind/holidays/pt/08.rem
/usr/share/remind/holidays/pt/09.rem
/usr/share/remind/holidays/pt/10.rem
/usr/share/remind/holidays/pt/12.rem
/usr/share/remind/holidays/pt/13.rem
/usr/share/remind/holidays/pt/14.rem
/usr/share/remind/holidays/pt/15.rem
/usr/share/remind/holidays/pt/16.rem
/usr/share/remind/holidays/pt/18.rem
/usr/share/remind/holidays/pt/20.rem
/usr/share/remind/holidays/pt/30.rem
/usr/share/remind/holidays/pw.rem
/usr/share/remind/holidays/py.rem
/usr/share/remind/holidays/ro.rem
/usr/share/remind/holidays/rs.rem
/usr/share/remind/holidays/ru.rem
/usr/share/remind/holidays/sa.rem
/usr/share/remind/holidays/sc.rem
/usr/share/remind/holidays/se.rem
/usr/share/remind/holidays/sg.rem
/usr/share/remind/holidays/si.rem
/usr/share/remind/holidays/sk.rem
/usr/share/remind/holidays/sm.rem
/usr/share/remind/holidays/sv.rem
%dir /usr/share/remind/holidays/sv
/usr/share/remind/holidays/sv/ss.rem
/usr/share/remind/holidays/sz.rem
/usr/share/remind/holidays/td.rem
/usr/share/remind/holidays/th.rem
/usr/share/remind/holidays/tl.rem
/usr/share/remind/holidays/tn.rem
/usr/share/remind/holidays/to.rem
/usr/share/remind/holidays/tr.rem
/usr/share/remind/holidays/tw.rem
/usr/share/remind/holidays/tz.rem
/usr/share/remind/holidays/ua.rem
/usr/share/remind/holidays/uk
/usr/share/remind/holidays/uk.rem
/usr/share/remind/holidays/um.rem
/usr/share/remind/holidays/us.rem
%dir /usr/share/remind/holidays/us
/usr/share/remind/holidays/us/ak.rem
/usr/share/remind/holidays/us/al.rem
/usr/share/remind/holidays/us/ar.rem
/usr/share/remind/holidays/us/as.rem
/usr/share/remind/holidays/us/az.rem
/usr/share/remind/holidays/us/ca.rem
/usr/share/remind/holidays/us/co.rem
/usr/share/remind/holidays/us/ct.rem
/usr/share/remind/holidays/us/dc.rem
/usr/share/remind/holidays/us/de.rem
/usr/share/remind/holidays/us/fl.rem
/usr/share/remind/holidays/us/ga.rem
/usr/share/remind/holidays/us/gu.rem
/usr/share/remind/holidays/us/hi.rem
/usr/share/remind/holidays/us/ia.rem
/usr/share/remind/holidays/us/id.rem
/usr/share/remind/holidays/us/il.rem
/usr/share/remind/holidays/us/in.rem
/usr/share/remind/holidays/us/ks.rem
/usr/share/remind/holidays/us/ky.rem
/usr/share/remind/holidays/us/la.rem
/usr/share/remind/holidays/us/ma.rem
/usr/share/remind/holidays/us/md-extra.rem
/usr/share/remind/holidays/us/md.rem
/usr/share/remind/holidays/us/me.rem
/usr/share/remind/holidays/us/mi.rem
/usr/share/remind/holidays/us/mo.rem
/usr/share/remind/holidays/us/mp.rem
/usr/share/remind/holidays/us/ms.rem
/usr/share/remind/holidays/us/nc.rem
/usr/share/remind/holidays/us/ne.rem
/usr/share/remind/holidays/us/nh.rem
/usr/share/remind/holidays/us/nj.rem
/usr/share/remind/holidays/us/nm.rem
/usr/share/remind/holidays/us/nv.rem
/usr/share/remind/holidays/us/ny.rem
/usr/share/remind/holidays/us/ok.rem
/usr/share/remind/holidays/us/pa.rem
/usr/share/remind/holidays/us/pr.rem
/usr/share/remind/holidays/us/ri.rem
/usr/share/remind/holidays/us/sc.rem
/usr/share/remind/holidays/us/sd.rem
/usr/share/remind/holidays/us/tn.rem
/usr/share/remind/holidays/us/tx.rem
/usr/share/remind/holidays/us/ut.rem
/usr/share/remind/holidays/us/va.rem
/usr/share/remind/holidays/us/vi.rem
/usr/share/remind/holidays/us/vt.rem
/usr/share/remind/holidays/us/wi.rem
/usr/share/remind/holidays/us/wv.rem
/usr/share/remind/holidays/uy.rem
/usr/share/remind/holidays/uz.rem
/usr/share/remind/holidays/va.rem
/usr/share/remind/holidays/ve.rem
/usr/share/remind/holidays/vi.rem
/usr/share/remind/holidays/vn.rem
/usr/share/remind/holidays/vu.rem
/usr/share/remind/holidays/ws.rem
/usr/share/remind/holidays/za.rem
/usr/share/remind/holidays/zm.rem

/usr/share/remind/lang/auto.rem
/usr/share/remind/moonphases.rem
/usr/share/remind/seasons.rem
/usr/share/remind/site/README
/usr/share/applications/tkremind.desktop
/usr/share/pixmaps/tkremind.png
%lang(ca) /usr/share/remind/lang/ca.rem
%lang(da) /usr/share/remind/lang/da.rem
%lang(de) /usr/share/remind/lang/de.rem
%lang(en) /usr/share/remind/lang/en.rem
%lang(es) /usr/share/remind/lang/es.rem
%lang(fi) /usr/share/remind/lang/fi.rem
%lang(fr) /usr/share/remind/lang/fr.rem
%lang(fr) /usr/share/remind/lang/gr.rem
%lang(is) /usr/share/remind/lang/is.rem
%lang(it) /usr/share/remind/lang/it.rem
%lang(nl) /usr/share/remind/lang/nl.rem
%lang(no) /usr/share/remind/lang/no.rem
%lang(pl) /usr/share/remind/lang/pl.rem
%lang(pt) /usr/share/remind/lang/pt.rem
%lang(ro) /usr/share/remind/lang/ro.rem

%changelog
