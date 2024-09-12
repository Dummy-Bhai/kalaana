import aiml
kernel=aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("LOAD")
while True:
    print(kernel.respond(input("Enter the message: ")))
