from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Your task is to develop a simple mail client that sends email to any recipient.
    # Your client will need to connect to a mail server, dialogue with the mail server
    # using the SMTP protocol, and send an email message to the mail server.
    # First, the client SMTP (running on the sending mail server host) has TCP establish a
    # connection to port 25 at the server SMTP (running on the receiving mail server host).

    # Once this connection is established, the server and client perform some application layer
    # handshaking before transferring information from one to another, SMTP clients and servers
    # introduce themselves before transferring information.

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    #serverName = 'smtp.nyu.edu'
    serverName = 'smtp.verizon.net'
    serverPort = 25

    #HANDSHAKING
    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024)
    recv = recv.decode()
    print(recv) #You can use these print statement to validate return codes from the server.
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Dean Matthews\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024)
    recv1 = recv1.decode()
    print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    #TRANSFER MESSAGES
    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailFrom = "MAIL FROM:<drm9114@nyu.edu>\r\n"
    clientSocket.send(mailFrom.encode())
    recv1 = clientSocket.recv(1024)
    recv1 = recv1.decode()
    if recv1[:3] != '250':
        print('250 reply not received from server.')
    # print("After MAIL FROM command: " + recv1)
    # Fill in end
    print("Sent MAIL FROM")
    # Send RCPT TO command and handle server response.

    # Fill in start
    mailtoCommand = 'RCPT TO:<dean.matthews@verizon.net> \r\n'
    clientSocket.send(mailtoCommand.encode())
    recv1 = clientSocket.recv(1024)
    recv1 = recv1.decode()
    print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end
    print("Sent RCPT TO")

    # Send DATA command and handle server response.
    # Fill in start
    senddataCommand = 'DATA\r\n'
    clientSocket.send(senddataCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1)
    if recv1[:3] != '354':
        print('354 reply not received from server.')
    # Fill in end
    print("Sent DATA")

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode())
    # Fill in end

    #CLOSURE
    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv1 = clientSocket.recv(1024).decode()
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    endCommand = 'QUIT \r\n'

    clientSocket.send(endCommand.encode())

    recv1 = clientSocket.recv(1024)
    recv1 = recv1.decode()

    print(recv1)

    if recv1[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')