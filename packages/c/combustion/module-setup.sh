depends() {
	echo bash network systemd url-lib
}

install() {
	inst_simple "${moddir}/combustion.service" "${systemdsystemunitdir}/combustion.service"
	inst_simple "${moddir}/combustion-prepare.service" "${systemdsystemunitdir}/combustion-prepare.service"
	inst_simple "${moddir}/combustion.rules" "/etc/udev/rules.d/70-combustion.rules"
	mkdir -p "${initdir}/${systemdsystemunitdir}/initrd.target.requires/"
	ln_r "../combustion.service" "${systemdsystemunitdir}/initrd.target.requires/combustion.service"
	inst_multiple awk chroot findmnt rmdir
	inst_simple "${moddir}/combustion" "/usr/bin/combustion"

	# Wait up to 10s (30s on aarch64) for the config drive
	devtimeout=10
	[ "$(uname -m)" = "aarch64" ] && devtimeout=30
	mkdir -p "${initdir}/${systemdsystemunitdir}/dev-combustion-config.device.d/"
	echo -e "[Unit]\nJobTimeoutSec=${devtimeout}" > "${initdir}/${systemdsystemunitdir}/dev-combustion-config.device.d/timeout.conf"
}
