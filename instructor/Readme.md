Instructor Setup
---

1. Deploy a Data Science Virtual Machine (Ubuntu), used in the second day - NC6 or NC12 SKU
2.  Log in to the DSVM or use a terminal window through Jupyterhub to run the `dsvm_setup.sh` script to make multiple user logins.
    * The usernames and passwords are stored under `/home/userinfo.csv` - download and distribute to attendees.  10 users are created with this script.  If more users are needed, more DSVMs should be provisioned.
    * `sudo usermod -aG docker USER` for all users and then restart VM (needed to test local deployments)

