.PHONY: install

install:
	install -p -m 0755 -d $(DESTDIR)/usr/lib/systemd/system
	install -p -m 0755 -D fake-hwclock $(DESTDIR)/usr/sbin/fake-hwclock
	install -p -m 0644 -D debian/fake-hwclock-load.service $(DESTDIR)/usr/lib/systemd/system/fake-hwclock-load.service
	install -p -m 0644 -D debian/fake-hwclock-save.service $(DESTDIR)/usr/lib/systemd/system/fake-hwclock-save.service
	install -p -m 0644 -D debian/fake-hwclock-save.timer $(DESTDIR)/usr/lib/systemd/system/fake-hwclock-save.timer
	install -p -m 0644 -D etc/default/fake-hwclock $(DESTDIR)/etc/default/fake-hwclock
	install -p -m 0644 -D fake-hwclock.8 $(DESTDIR)/usr/share/man/man8/fake-hwclock.8
