Running gaccess perodically
===========================

1. Create an `/etc/goaccess/example.conf`

   Set the following variables:

   * `log-format`
   * `html-report-title`
   * `log-file`
   * `output`

2. Start the systemd timer for the instance

       systemctl enable --now goaccess@example.timer
