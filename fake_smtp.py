import smtpd
import asyncore
import time

class FakeSMTPServer(smtpd.SMTPServer):
  def __init__(*args, **kwargs):
    print('Running fake smtp server on port 8025')
    smtpd.SMTPServer.__init__(*args, **kwargs)

  def process_message(*args, **kwargs):
    mail = open('mails/' + str(time.time()) + '.eml', 'w')
    print('New mail from ' + args[2])
    print('Data:' + args[4].decode())
    mail.write(args[4].decode())
    mail.close
    pass

if __name__ == '__main__':
  smtp_server = FakeSMTPServer(('0.0.0.0', 8025), None)
  try:
    asyncore.loop()
  except KeyboardInterrupt:
    smtp_server.close()
