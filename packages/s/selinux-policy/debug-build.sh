# This script creates a debugging and testing environment when working on the policy
# Basically a fancy wrapper for "tar --exclude-vcs -cJf selinux-policy-20230321.tar.xz --transform 's,^,selinux-policy-20230321/,' -C selinux-policy ."
# 
# 1. Get the git repository with 'osc service manualrun' or './update.sh'
# 2. Do your changes in the selinux-policy repository, test around
# 	1. When you want to build locally to debug, call this script. It will create a .tar.xz with your current selinux-policy working directory.
# 	2. Build locally: e.g. with osc build
#	3. Test your rpms that contain your changes and repeat 
# 3. When finished, commit your changes in the selinux-policy repository and push to git
# 4. Run './update.sh' and checkin the changes to OBS

REPO_NAME=selinux-policy

# Check if git repository exists, if not ask the user to fetch the latest version 
if ! test -d "$REPO_NAME"; then
    	echo "-$REPO_NAME does not exist. Please run 'osc service manualrun' or './update.sh' first."
	exit 1;
fi

# Get current version: Parse "Version: <current-version>" from specfile
VERSION=$(grep -Po '^Version:\s*\K.*?(?=$)' $REPO_NAME.spec)

# Create tar file with name like selinux-policy-<current-version>.tar.xz 
TAR_NAME=$REPO_NAME-$VERSION.tar.xz
echo "Creating tar file: $TAR_NAME"
tar --exclude-vcs -cJhf $TAR_NAME --transform "s,^,$REPO_NAME-$VERSION/," -C $REPO_NAME .

# Some helpful prompts
if test $? -eq 0; then 
	echo "Success! Now you can run your local build command, e.g. 'osc build'. It will take the archive that contains your changes."
	echo "You can also inspect the created archive with: 'tar tvf $REPO_NAME-$VERSION.tar.xz'"
else
	echo "Error, creating archive failed"
fi
