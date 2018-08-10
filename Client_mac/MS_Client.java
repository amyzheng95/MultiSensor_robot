import java.net.*;
import java.io.*;
import java.util.*;

public class MS_Client
{

	private String hostName = "raspberrypi.local";
	private int port = 4242; 
	private Socket socket;
	private InputStream in;
	private OutputStream out;
	private StringBuffer stringBuffer;
	private DataInputStream dataInputStream;
	private DataOutputStream dataOutputStream;
	private BufferedReader socketReader;
	private BufferedWriter socketWriter;
	private BufferedReader stdIn;
	private PrintWriter pWriter;

	public static void main(String[] args)
	{
		MS_Client client = new MS_Client();
		client.checkCommandLineInput(args);
		client.connectToServer();
		//System.out.println("waiting data: " + client.checkWaitingData());
		client.sendSomething();
		//client.getUserInput();
	}

	public void checkCommandLineInput(String[] args)
	{
		if(args.length == 1)
		{
			port = Integer.parseInt(args[0]);
		}
		else if(args.length == 2)
		{
			hostName = args[0];
			port = Integer.parseInt(args[1]);
		}
	}

	public boolean checkWaitingData()
	{	
		boolean waitingData = false;
		if(dataInputStream == null){
			try
			{
				dataInputStream = new DataInputStream(socket.getInputStream());
				System.out.println("Opening input stream");
			}
			catch(Exception e)
			{		
				System.err.println(e);
				System.err.println("error");
			}
		}
		try
		{
			if(dataInputStream.available()>0)
			{
				waitingData = true;	
				System.out.println("bytes available: " + dataInputStream.available());
			}
			else
			{
				System.out.println("No bytes available");
			}
		}
		catch(Exception e)
		{		
			System.err.println(e);
			System.err.println("error");
		}
		return waitingData;
	}

	public void connectToServer()
	{
		System.out.println("Connecting to" + this.hostName + "at port" + this.port);
		try
		{
			socket = new Socket(this.hostName,this.port);
			System.out.println("Connected");
		}
		catch(UnknownHostException ex)
		{
			System.err.println(ex);
			System.err.println("Error: does not know host" + hostName);
		}
		catch(IOException ex)
		{
			System.err.println(ex);
		}
		
	}

	public void getInputFromServer()
	{
		try
		{
			System.out.println("are you here?");	
			in = socket.getInputStream();
			stringBuffer = new StringBuffer();
			int c;
			while((c=in.read())!=-1)
			{ 
				stringBuffer.append((char) c);
			}			
			String string = stringBuffer.toString();
			System.out.println(string);
			System.out.println("worked");
		}
		catch(IOException ex)
		{
			System.err.println(ex);
		}
	}

	public void sendSomething()
	{
		try
		{
			socketReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
			stdIn = new BufferedReader(new InputStreamReader(System.in));
			pWriter = new PrintWriter(socket.getOutputStream(),true);
			
			String fromServer;
			String fromUser = "";
			
			while((fromServer = socketReader.readLine())!=null && (! fromServer.isEmpty()))
			{
				System.out.println(fromServer);
				
			}
			
			while(!fromUser.equals("q"))
			{
				System.out.println("Please enter a command");

				fromUser = stdIn.readLine();
				if(fromUser!=null)
				{
					System.out.println("Client: " + fromUser);
					pWriter.println(fromUser);
				}	
				
				if((fromServer = socketReader.readLine())!=null && (! fromServer.isEmpty()))
				{
					System.out.println(fromServer);
				}
				/*
				if(fromUser.equals("q"))
				{
					try{
						socket.close();
						
					}
				}
				*/		
			}
			pWriter.println(fromUser);
			
		}catch(IOException e)
		{
			System.err.println("IOException");
		}

	}
/*	
	public void askForCommand()
	{
		try
		{
			//System.out.println("Send a command to the Server:");
			//String userInput = inReader.readLine();
			//writer.write(userInput);
			//writer.newLine(); 
			//writer.flush();
		}
		catch(IOException ex)
		{}
	}

*/
			/*
			System.out.println("Welcome to the MultiSensor Robot Server");
			System.out.println("Menu");
			System.out.println("s - get sensor values");
			System.out.println("f - go straight");
			System.out.println("b - go backwards");
			System.out.println("l - go left");
			System.out.println("r - go right");
			System.out.println("p - take a pic");	
			*/
}
