#!/bin/bash

set -e

while getopts "u:p:d:h" opt; do
  case ${opt} in
    u)
      USERNAME="${OPTARG}"
      ;;
    p)
      PASSWORD="${OPTARG}"
      ;;
    d)
      HOMEDIR="${OPTARG}"
      ;;
    h|*)
      ME=$(basename "$0")
      echo "Usage:" >&2
      echo "  $ME -u <username> -p <password> [-d <path>]" >&2
      exit 1
      ;;
  esac
done

if [[ -z "$USERNAME" ]]; then
  echo "Username missing." >&2
  exit 1
fi

if [[ -z "$PASSWORD" ]]; then
  echo "Password missing." >&2
  exit 1
fi

if [[ -z "$HOMEDIR" ]]; then
  HOMEDIR="/home/$USERNAME"
fi

if ! id "$USERNAME" &>/dev/null; then
  echo "Adding system user: $USERNAME"
  useradd -M -U -d "$HOMEDIR" -s /usr/bin/false "$USERNAME"
  mkdir -p "$HOMEDIR"
  chown "$USERNAME":"$USERNAME" "$HOMEDIR"
else
  echo "User $USERNAME already exists, skipping user creation."
fi

echo "Setting Samba password for user: $USERNAME"
(echo "$PASSWORD"; echo "$PASSWORD") | smbpasswd -s -a "$USERNAME"
