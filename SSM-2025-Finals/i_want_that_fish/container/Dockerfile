# Setting up chroot below
FROM ubuntu:20.04 AS chroot

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get upgrade -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y python3-pip && \
    python3 -m pip install pycryptodome && \
    pip install bcrypt
    #python3 -m pip install hashlib

RUN groupadd -g 1337 ctf && useradd -r -u 1337 -g ctf ctf
RUN mkdir -p /home/ctf/

COPY apparatus.py /home/ctf/
COPY merchant.py /home/ctf/
RUN chmod +x /home/ctf/apparatus.py

# Now setting up the actual container
FROM ghcr.io/google/nsjail/nsjail:latest

COPY --from=chroot / /chroot

ENTRYPOINT nsjail --port 1337 --chroot /chroot/ --user 1337 --group 1337 --cwd /home/ctf/ --tmpfsmount /tmp --bindmount_ro /etc/resolv.conf:/etc/resolv.conf /home/ctf/apparatus.py
