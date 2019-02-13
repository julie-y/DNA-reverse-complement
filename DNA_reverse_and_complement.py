#ask to input DNA sequence

  #reverse
def reverse(sequence):
      sequence = sequence[::-1]
      return sequence

while True:
  sequence =input('Please type in your DNA sequence:').strip().lower()
  print ('Your original sequence is: {}'.format(sequence))
  new_sequence =reverse (sequence)

#compliment                
  output = new_sequence.replace ('a','T').replace('t','A').replace('g','C').replace('c','G')
  output=output.lower()
  print ('Your reverse/complement sequence is: {}.'.format(output))
