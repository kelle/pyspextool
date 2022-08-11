def loopprogress(idx, bot, top, message=None):

    """
    To print a loop update message on the command line

    Parameters
    ----------------
    idx : int
          the current loop index number, e.g. i

    bot : int
          the bottom of the loop, e.g. range(bot,top)

    top : int
          the bottom of the loop, e.g. range(bot,top)

    message : str
              A string to print before the update begin, optional.

    Returns
    --------
    None

    Procedure
    ---------
    Just prints a updating message on the command line

    Example
    --------
    >>> loopprogress(i,0,100)
     90% |*************************************                       |


    Modification History
    --------------------
    2022-05-25 - Written by M. Cushing, University of Toledo.
                Based on the Spextool mc_loopprogress.pro IDL program.
    """
    
    # Print the message if necessary
    
    if idx == 0 and message is not None:

        print(message)

    # Run counter        
            
    frac = (idx+1-bot)/(top-bot)
    stars = "{:<70}".format('*'*round(frac*70))
    print(str(round(frac*100)).rjust(3), '% ', '|', stars, '|',
          sep='', end='\r')

    # Now get your prompt back

    if idx == top-1:

        print()
